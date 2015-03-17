from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^register/', 'forum.views.register'),
    url(r'^login/', 'forum.views.login'),
    url(r'^logout/', 'forum.views.logout'),

    url(r'^forum/', 'forum.views.forum'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'forum.views.home'),
)
