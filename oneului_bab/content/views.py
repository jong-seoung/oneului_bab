from django.shortcuts import render
from django.views.generic import TemplateView
from content.models import FoodList
from rest_framework.response import Response
from django.db.models import Q
from .models import FoodList

class Index(TemplateView):
    template_name = 'index.html'

class Main(TemplateView):
    template_name = 'content/main.html'
    
    def post(self, request):
        if request.method == 'POST':
            result_mune_lst = request.POST
            a = Q()
            b = Q()
            c = Q()
            d = Q()
            e = Q()
            print(result_mune_lst)
            for i in result_mune_lst:
                if i == "main_all" or i == "noodle" or i == "rice" or i == "bread":
                    if i == "main_all":
                        a.add(Q(main="noodle")|Q(main="rice")|Q(main="bread"), a.AND)
                    elif i == "noodle":
                        a.add(Q(main="noodle"), a.OR)
                    elif i == "rice":
                        a.add(Q(main="rice"), a.OR)
                    elif i == "bread":
                        a.add(Q(main="bread"), a.OR)

                elif i == "soup_all" or i == "yes" or i == "little" or i == "no":
                    if i == "soup_all":
                        b.add(Q(soup="yes")|Q(soup="little")|Q(soup="no"), b.AND)
                    elif i == "yes":
                        b.add(Q(soup="yes"), b.OR)
                    elif i == "little":
                        b.add(Q(soup="little"), b.OR)
                    elif i == "no":
                        b.add(Q(soup="no"), b.OR)

                elif i == "Spicy_all" or i == "spicy" or i == "normal" or i == "mild":
                    if i == "Spicy_all":
                        c.add(Q(Spicy="spicy")|Q(Spicy="normal")|Q(Spicy="mild"), c.AND)
                    elif i == "spicy":
                        c.add(Q(Spicy="spicy"), c.OR)
                    elif i == "normal":
                        c.add(Q(Spicy="normal"), c.OR)
                    elif i == "mild":
                        c.add(Q(Spicy="mild"), c.OR)

                elif i == "temperature_all" or i == "cool" or i == "hot":
                    if i == "temperature_all":
                        d.add(Q(temperature="cool")|Q(temperature="hot"), d.AND)
                    elif i == "cool":
                        d.add(Q(temperature="cool"), d.OR)
                    elif i == "hot":
                        d.add(Q(temperature="hot"), d.OR)

                elif i == "weight_all" or i == "heavy" or i == "light":
                    if i == "weight_all":
                        e.add(Q(weight="heavy")|Q(weight="light"), e.AND)
                    elif i == "heavy":
                        e.add(Q(weight="heavy"), e.OR)
                    elif i == "light":
                        e.add(Q(weight="light"), e.OR)
            FoodList_results = FoodList.objects.filter(a,b,c,d,e)
            print(a,b,c,d,e)
            print(FoodList_results)
            print("1")
            return render(request,'content/main.html',{'FoodList_results':FoodList_results})
        else:
            print("2")
            return render(request,'content/main.html', {})

def result(request):
    return render(request,'content/result.html')

class Recommend(TemplateView):
    template_name = 'content/recommend.html'
