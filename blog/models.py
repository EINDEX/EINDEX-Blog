from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
import markdown
from django.utils.html import strip_tags


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)

    author = models.ForeignKey(User)

    is_publish = models.BooleanField(default=False)
    html = models.TextField(editable=False, blank=True)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.html = md.convert(self.body)

        if not self.excerpt:
            self.excerpt = strip_tags(md.convert(self.body))[:200]
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_time', 'title']
