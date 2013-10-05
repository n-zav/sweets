from django.conf.urls import patterns, include, url
from sweets.views import HomePageView, AboutView
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                      (r'^$', HomePageView.as_view()),
                      (r'^about/', AboutView.as_view()),
    # Examples:
    # url(r'^$', 'sweets.views.home', name='home'),
    # url(r'^sweets/', include('sweets.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
