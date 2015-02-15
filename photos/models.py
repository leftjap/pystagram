# coding: utf-8

from django.db import models
from django.conf import settings

class Photo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    image_file = models.ImageField()
    is_active = models.BooleanField(default=True)
    tags = models.ManyToManyField('Tag')
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return u"{0} - '{1}'".format(self.id, self.user)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ForeignKey(Photo)
    content = models.TextField(null=False, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return u"{0} 'photo:{1}'".format(self.id, self.photo.id)

class Tag(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return u"{0}".format(self.name)