from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'index.html'

class Main(TemplateView):
    template_name = 'content/main.html'


class Recommend(TemplateView):
    template_name = 'content/recommend.html'
