from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.views import View
from .forms import ContactForm


class HomeView(View):
    template_name = 'landingpage/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('/feed/')
        return render(request, self.template_name)

# Create your views here.
class ContactView(View):
    template_name = 'landingpage/contact.html'
    class_form = ContactForm
    sent = False

    def get(self, request):
        form = self.class_form()
        return render(request, self.template_name, {'form': form, 'sent': self.sent})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            inputs = form.cleaned_data
            subject = 'Message from {} {} via contact form'\
                .format(inputs['first_name'], inputs['last_name'])
            email = inputs['email']
            message = str(inputs['message']) + "\nMessage from " + str(email) #google's SMTP does not allow to change from email field
            to = ['alumate.info@gmail.com','snishino2013@gmail.com']
            send_mail(subject, message, email, to)
            self.sent = True
            form = self.class_form()
        return render(request, self.template_name, {'form': form, 'sent': self.sent})