from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'vote_app.views.home', name='home'),
    url(r'^about/', 'vote_app.views.about', name='about'),
    url(r'^vote/', 'vote_app.views.vote', name='vote'),

    url(r'^view/$', 'vote_app.views.view_home', name='view_home'),
    url(r'^view/(?P<discussion_id>\d+)/$', 'vote_app.views.view', name='view'),

    # url(r'^voting_project/', include('voting_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
