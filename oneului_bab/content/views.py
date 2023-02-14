from django.shortcuts import render
from django.views.generic import TemplateView
from content.models import FoodList

class Index(TemplateView):
    template_name = 'index.html'

class Main(TemplateView):
    template_name = 'content/main.html'
    queryset = FoodList.objects.all()

    def get(self, request, *args, **kwargs):
        print(request.GET)
        ctx = {
            'FoodLists': self.queryset
        }
        return self.render_to_response(ctx)

class Recommend(TemplateView):
    template_name = 'content/recommend.html'
