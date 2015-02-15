from django.conf.urls import patterns, include, url
from django.contrib import admin
from photos import urls as photo_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^photos/', include(photo_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/login/'}),
    url(r'^signup/$', 'profiles.views.signup'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)