from django.conf.urls import patterns, url

urlpatterns = patterns('photos.views',
    url(r'^$', 'toppage', name='photo_toppage'),
    url(r'^(?P<photo_id>[0-9]+)/$', 'single_photo'),
    url(r'^create/$', 'edit_photo'),
)