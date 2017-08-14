# Create your views here.
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.dates import MonthArchiveView

from blog.models import Post
from blog.models import Tag


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 10
    number_of_pages_show = 4

    queryset = Post.objects.filter(is_publish=True)

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = self.pagination_data(paginator, page, is_paginated)

        context.update(pagination_data)

        return context

    def pagination_data(self, paginator, page, is_paginated):
        NOPS = self.number_of_pages_show
        if not is_paginated:
            return {}

        left = []
        right = []

        first = False
        last = False

        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range

        if page_number == 1:
            first = True
        if page_number == total_pages:
            last = True
        left = page_range[0 if page_number - NOPS < 0 else page_number - NOPS:page_number - 1]
        right = page_range[page_number:total_pages if page_number + NOPS > total_pages else page_number + NOPS]

        data = {
            'left': left,
            'right': right,
            'first': first,
            'last': last,
        }
        return data


class TagView(IndexView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()

        return response

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=None)
        if not post.is_publish:
            raise Http404()
        return post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post = context.get('post')

        post_pn_data = self.get_post_prev_and_next(post)

        context.update(post_pn_data)
        return context

    def get_post_prev_and_next(self, post):
        p = Post.publish_objects.filter(created_time__gt=post.created_time).last()
        n = Post.publish_objects.filter(created_time__lt=post.created_time).first()
        return {
            'prev': p,
            'next': n,
        }


# 归档
class ArchiveView(MonthArchiveView):
    queryset = Post.publish_objects.all()
    date_field = 'created_time'
    model = Post
    make_object_list = True
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


def page404(request):
    return render(request, '404.html')


def page500(request):
    return render(request, '500.html')
