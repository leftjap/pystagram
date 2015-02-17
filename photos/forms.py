# coding: utf-8

from django import forms
from .models import Photo, Comment

class PhotoModelForm(forms.ModelForm):
    tags = forms.CharField(required=False, max_length=200)
    class Meta:
        model = Photo
        fields = ('image_file', 'tags', 'description',)


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

