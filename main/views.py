from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from main.models import ContactModel


class AboutAsView(TemplateView):
    template_name = 'main/about.html'


class ContactView(CreateView):
    model = ContactModel
    fields = ['name', 'email', 'message']
    template_name = 'main/contact.html'

    def get_success_url(self):
        return reverse('contact')
# Create your views here.


class HomeView(TemplateView):
    template_name = 'main/index.html'
