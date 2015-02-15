# coding: utf-8

from django import forms
from .models import Photo

class PhotoModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image_file', 'description',)


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        