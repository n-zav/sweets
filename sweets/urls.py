from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from sweets.views import HomePageView, contact
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', HomePageView.as_view(), name='home'),
                       url(r'^about/', TemplateView.as_view(template_name="about.html"),
                           name='about'),
                       url(r'^contact/', contact, name='contact'),
                       url(r'^thanks/', TemplateView.as_view(template_name="thanks.html"),
                           name='thanks'),
    # Examples:
    # url(r'^$', 'sweets.views.home', name='home'),
    # url(r'^sweets/', include('sweets.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
