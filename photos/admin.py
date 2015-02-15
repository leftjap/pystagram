# coding: utf-8

from django.contrib import admin

from photos.models import Photo

admin.site.register(Photo)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_active', 'created_at', 'updated_at',)
    ordering = ('-id', 'updated_at',)