from django.conf.urls import patterns, url
from climbgupiao import views

 
urlpatterns = patterns('',
    url(r'^$', views.search, name='search'),
    url(r'^search/$',views.search,name = 'search'),
)