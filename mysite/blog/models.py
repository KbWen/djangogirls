# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.core.urlresolvers import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)

    content = models.TextField(blank=True)
    excerpt = models.CharField(max_length=50, blank=True)

    photo = models.URLField(blank=True)

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)

    author = models.ForeignKey(User)

    views = models.PositiveIntegerField(default=0)

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.excerpt:
            self.excerpt = strip_tags(self.content)[:20]

        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['created_time']

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})