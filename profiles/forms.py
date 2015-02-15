# coding: utf-8

from django import forms

from profiles.models import Profile

class ProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = Profile
        fields = ('gender', )