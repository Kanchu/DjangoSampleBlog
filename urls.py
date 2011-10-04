from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'blog.views.index'),
     url(r'^home','blog.views.home',name='home'),
     url(r'^add','blog.views.add',name='add'),
     url(r'^feedback','blog.views.feedback',name='feedback'),
     url(r'^list_feedback','blog.views.list_feedback',name='list_feedback'),
     url(r'^detail/(?P<id>\d+)$', 'blog.views.detail', name='detail'),
     url(r'^delete/(?P<id>\d+)$', 'blog.views.delete', name='delete'),
     url(r'^del_feed/(?P<id>\d+)/$', 'blog.views.del_feed', name='del_feed'),
#     url(r'^delete/(?P<id>\d+)/$', 'blog.views.delete', name='delete'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
