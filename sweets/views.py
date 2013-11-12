from django.shortcuts import render
from django.http import HttpResponseRedirect
from sweets.forms import ContactForm
from sortable_listview import SortableListView
from sweets.models import Product
from django.utils.translation import ugettext_lazy as _


def feedback(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']

            recipients = ['nastya.zavalkina@gmail.com']

            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form

    return render(request, 'feedback.html', {
        'form': form,
    })


class ProductListView(SortableListView):
    allowed_sort_fields = {'name': {'default_direction': '', 'verbose_name': _('Product name')},
                           'date': {'default_direction': '-','verbose_name': _('Date added')},
                           'price': {'default_direction': '-','verbose_name': _('Price')}}
    default_sort_field = 'date'
    paginate_by = 5
    template_name = 'index.html'
    model = Product
