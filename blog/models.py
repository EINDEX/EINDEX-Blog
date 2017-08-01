import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
import markdown
from django.utils.html import strip_tags
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from markdown_checklist.extension import ChecklistExtension
from editormd.models import EditorMdField


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PostPublishManager(models.Manager):
    def get_queryset(self):
        return super(PostPublishManager, self).get_queryset().filter(is_publish=True)


class Post(models.Model):
    title = models.CharField(max_length=70)

    body = EditorMdField()

    created_time = models.DateTimeField(blank=True)
    modified_time = models.DateTimeField(blank=True)

    slug = models.SlugField(max_length=50, unique=True)

    excerpt = models.CharField(max_length=200, blank=True)

    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(editable=False, default=0)

    author = models.ForeignKey(User, on_delete='SET_DEFAULT', default=User.objects.first())

    is_publish = models.BooleanField(editable=False, default=False)
    # 展示用
    html = models.TextField(editable=False, blank=True)
    toc = models.TextField(editable=False, blank=True)

    # 查询器
    objects = models.Manager()
    publish_objects = PostPublishManager()

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            ChecklistExtension(),
            TocExtension(slugify=slugify),
        ])
        if not self.created_time:
            self.created_time = datetime.datetime.now()
        self.modified_time = datetime.datetime.now()
        self.html = md.convert(self.body)
        self.toc = md.toc
        if not self.excerpt:
            self.excerpt = strip_tags(md.convert(self.body))[:200]
        super(Post, self).save(*args, **kwargs)

    @property
    def identifier(self):
        return 'post_%s' % self.pk

    class Meta:
        ordering = ['-created_time', 'title']
