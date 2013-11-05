from django.views.generic import TemplateView

from django.shortcuts import render
from django.http import HttpResponseRedirect
from sweets.forms import ContactForm


class HomePageView(TemplateView):
    template_name = "index.html"


def contact(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = ContactForm(request.POST)  # A form bound to the POST data
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['email']

            recipients = ['nastya.zavalkina@gmail.com']

            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')  # Redirect after POST
    else:
        form = ContactForm() # An unbound form

    return render(request, 'contacts.html', {
        'form': form,
    })
