from django.shortcuts import render
from django.views.generic import TemplateView


class AboutUs(TemplateView):
    http_method_names = ['get', 'post']
    template_name = 'about.html'
    extra_context = {}


class Contact(TemplateView):
    http_method_names = ['get', 'post']
    template_name = 'contact.html'
    extra_context = {}


class Services(TemplateView):
    http_method_names = ['get', 'post']
    template_name = 'services.html'
    extra_context = {}
