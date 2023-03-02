from django.shortcuts import render
from django.views.generic import TemplateView
from content.models import FoodList
from django.shortcuts import redirect
from django.db.models import Q
from .models import FoodList
import json
from django.shortcuts import render, redirect
from .models import Question

class Index(TemplateView):
    template_name = 'index.html'

class Main(TemplateView):
    template_name = 'content/main.html'

    def get(self, request):
        food_list_cookie = request.COOKIES.get('FoodList_results')
        if food_list_cookie:
            food_list = json.loads(food_list_cookie)
            selected_food_list = []
            for i in food_list:
                selected_food = i.get('name')
                selected_food_list.append(selected_food)
            return render(request, 'content/main.html', {'selected_food_list': selected_food_list})
        else:
            return render(request, 'content/main.html')

    def post(self, request):
        if request.method == 'POST':
            result_mune_lst = request.POST
            FoodList_results_list = []
            a = Q()
            b = Q()
            c = Q()
            d = Q()
            e = Q()
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

                elif i == "temperature_all" or i == "cool" or i == "warm" or i == "hot":
                    if i == "temperature_all":
                        d.add(Q(temperature="cool")|Q(temperature="warm")|Q(temperature="hot"), d.AND)
                    elif i == "cool":
                        d.add(Q(temperature="cool"), d.OR)
                    elif i == "warm":
                        d.add(Q(temperature="warm"), d.OR)
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
            FoodList_results_json = json.dumps(list(FoodList_results.values()))
            response = redirect('main')
            response.set_cookie('FoodList_results', FoodList_results_json)
            return response
        else:
            return render(request, 'content/main.html', {'FoodList_results':FoodList_results})


def recommend(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        main = request.POST.get('main')
        soup = request.POST.get('soup')
        spicy = request.POST.get('spicy')
        temperature = request.POST.get('temperature')
        weight = request.POST.get('weight')
        approved = False
        print(name,main,soup,spicy,temperature,weight,approved)
        FoodList.objects.create(name=name, main=main, soup=soup, Spicy=spicy, temperature=temperature, weight=weight, approved=approved)
        return redirect('recommendname')
    return render(request, 'content/recommend.html')

class Question_Answer(TemplateView):
    template_name = 'content/question.html'
    queryset = Question.objects.all()

    def get(self, request, *args, **kwargs):
        ctx = {
            'Questions': self.queryset		
        }
        return self.render_to_response(ctx)
    
    def post(self, request):
        if request.method == 'POST':
            title = request.POST['title']
            content = request.POST['content']
            Question.objects.create(title=title, content=content)
            return redirect('question')
        else:
            return render(request, 'content/question.html')
        