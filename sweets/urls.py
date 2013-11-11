from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, ListView
from sweets.views import feedback

from django.conf import settings
from sweets.models import Product

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       url(r'^$', ListView.as_view(model=Product, template_name="index.html"), name='home'),
                       url(r'^about/', TemplateView.as_view(template_name="about.html"),
                           name='about'),
                       url(r'^contact/', TemplateView.as_view(template_name="contacts.html"),
                           name='contact'),
                       url(r'^feedback/', feedback, name='feedback'),
                       url(r'^thanks/', TemplateView.as_view(template_name="thanks.html"),
                           name='thanks'),
                       url(r'^admin/', include(admin.site.urls)),

    # Examples:
    # url(r'^$', 'sweets.views.home', name='home'),
    # url(r'^sweets/', include('sweets.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
)