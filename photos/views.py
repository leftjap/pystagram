# coding: utf-8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.core.urlresolvers import reverse

from photos.models import Photo
from photos.forms import PhotoModelForm
from django.contrib.auth.decorators import login_required

def toppage(request):
    return HttpResponse('hello')

def single_photo(request, photo_id):
    if int(photo_id) == 0:
        return HttpResponseRedirect(reverse('photo_toppage'))

    photo = get_object_or_404(Photo, pk=photo_id)

    _res = render(
        request,
        'single_photo.html',
        {
            'photo': photo,
        }
    )
    _res['my_header'] = 'hannal'

    return _res

from photos.forms import PhotoModelForm

@login_required
def edit_photo(request, photo_id=None):
    if request.method == 'GET':
        form = PhotoModelForm()
    elif request.method == 'POST':
        form = PhotoModelForm(request.POST, request.FILES)

        if form.is_valid():
            _photo = form.save(commit=False)
            _photo.user = request.user
            _photo.save()

        return HttpResponseRedirect('/photos/{0}/'.format(_photo.id))

    return render(request, 'edit_photo.html', {
            'form': form,
        })
