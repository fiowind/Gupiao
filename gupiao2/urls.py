from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gupiao2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$', 'climbgupiao.views.search', name='search'),
    url(r'^search$', 'climbgupiao.views.search', name='search'),
    url(r'^codesearch$', 'climbgupiao.views.codesearch', name='codesearch'),
    url(r'^ajaxlist$', 'climbgupiao.views.ajaxlist', name='ajaxlist'),
)
