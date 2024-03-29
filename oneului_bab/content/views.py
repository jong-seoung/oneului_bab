from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Q
from .models import FoodList, Save, Question, Save_memo
from user.models import User
from rest_framework.views import APIView
import json
import os
from uuid import uuid4
from config.settings import MEDIA_ROOT
import random
from django.contrib import messages

# 인덱스 
class Index(TemplateView):
    template_name = 'index.html'

# 메인화면
class Main(TemplateView):
    template_name = 'content/main.html'

    def menu_filter(self, request):
        result_mune_lst = request.POST
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
            
        return [ a, b, c, d, e]
    
    def get(self, request):
        food_list_cookie = request.COOKIES.get('random_food_list')
        email = request.session.get('email',None)
        
        if food_list_cookie:
            food_list = json.loads(food_list_cookie)
            selected_food_list = []
            for i in food_list:
                save_count = Save.objects.filter(food_id=i.get('id'), is_save=True).count()
                is_saved = Save.objects.filter(food_id=i.get('id'), email=email,is_save=True).exists()
                selected_food_list.append({'name':i.get('name'),'image':i.get('image'),'food_id':i.get('id'),'save_count':save_count,'is_saved':is_saved})
            random.shuffle(selected_food_list)
            return render(request, 'content/main.html', {'selected_food_list': selected_food_list})
        else:
            return render(request, 'content/main.html')

    def post(self, request):

        if request.POST.get('clicked_button_id') == 'normal_button':
            menu_filter_result = self.menu_filter(request)
            a, b, c, d, e = menu_filter_result
            random_food_list = list(FoodList.objects.filter(a,b,c,d,e).values())
            random_food_list_json = json.dumps(random_food_list)
        elif request.POST.get('clicked_button_id') == 'random_button':
            menu_filter_result = self.menu_filter(request)
            a, b, c, d, e = menu_filter_result
            FoodList_results = list(FoodList.objects.filter(a,b,c,d,e).values())
            if len(FoodList_results) > 3:
                random_food_list = random.sample(FoodList_results, 3)
            elif len(FoodList_results) < 3:
                random_food_list = random.sample(FoodList_results, len(FoodList_results))
            random_food_list_json = json.dumps([food for food in random_food_list][:3])

        response = redirect('main')
        response.set_cookie('random_food_list', random_food_list_json)
        return response

# 추천하기
def recommend(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        main = request.POST.get('main')
        soup = request.POST.get('soup')
        spicy = request.POST.get('spicy')
        temperature = request.POST.get('temperature')
        weight = request.POST.get('weight')
        approved = False
        file = request.FILES.get('image')
        email = request.session.get('email',None)

        if email == None:     
            email = {'email':email}
            return HttpResponse(json.dumps(email), content_type="application/json")
        else:
            if file:
                uuid_name = uuid4().hex
                save_path = os.path.join(MEDIA_ROOT, uuid_name)

                # 파일을 읽어서 파일을 만들기
                with open(save_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

                image = uuid_name
            else:
                image = 'food_basic_img.jpg'
            
            FoodList.objects.create(name=name, main=main, soup=soup, Spicy=spicy, temperature=temperature, weight=weight, image=image, approved=approved)
            return redirect('recommendname')
    return render(request, 'content/recommend.html')

# 문의하기
class Question_Answer(TemplateView):
    template_name = 'content/question.html'
    queryset = Question.objects.all()

    def get(self, request, *args, **kwargs):
        messages.info(request,"문의하기")
        ctx = {
            'Questions': [
                {
                    'id': q.id,
                    'email': q.email,
                    'nickname': str(q.nickname)[:-2] + '**' if len(q.nickname) > 2 else str(q.nickname)[:-1] + '*',
                    'title': q.title,
                    'content': q.content,
                    'answer': q.answer,
                    'created_at': q.created_at.strftime('%Y년 %m월 %d일')
                }
                for q in self.queryset[::-1]
            ]
        }
        return self.render_to_response(ctx)
    
    def post(self, request):
        if request.POST.get('submit') == 'question_upload':
            title = request.POST['title']
            content = request.POST['content']
            email = request.session.get('email',None)
            ctx = {            
                'Questions': [
                {
                    'id': q.id,
                    'email': q.email,
                    'nickname': str(q.nickname)[:-2] + '**' if len(q.nickname) > 2 else str(q.nickname)[:-1] + '*',
                    'title': q.title,
                    'content': q.content,
                    'answer': q.answer,
                    'created_at': q.created_at.strftime('%Y년 %m월 %d일')
                }
                for q in self.queryset[::-1]
            ],
            'title':title,
            'content':content}
            if email == None:
                messages.error(request,"로그인이 필요한 기능입니다.")
                return redirect('loginview')
            if title == "":
                messages.error(request,"제목이 없습니다.")
                return HttpResponse(render(request, 'content/question.html', ctx))
            elif content == "":
                messages.error(request,"내용이 없습니다.")
                return HttpResponse(render(request, 'content/question.html', ctx))
            else:
                print("등록완료")
                user = User.objects.filter(email=email).first()
                nickname = user.nickname
                Question.objects.create(title=title, content=content,nickname=nickname,email=email)
                return redirect('question')
        else:
            return render(request, 'content/question.html')

# 저장기능
class ToggleSave(APIView):

    def post(self,request):
        food_id = request.data.get('food_id',None)
        save_text = request.data.get('save_text',True)
        email = request.session.get('email',None)

        if email == None:
            email = {'email':email}
            return HttpResponse(json.dumps(email), content_type="application/json")
        else:
            if save_text == '저장':
                is_save = True
            else:
                is_save = False

            save = Save.objects.filter(food_id=food_id,email=email).first()
            
            if save:
                save.is_save = is_save
                save.save()
            else:
                Save.objects.create(food_id=food_id, is_save=is_save,email=email)
                food = FoodList.objects.get(id=food_id)
                Save_memo.objects.create(food_id=food, memo="",email=email)
                
            
            save_count = Save.objects.filter(food_id=food_id, is_save=True).count()
            is_saved = Save.objects.filter(food_id=food_id, email=email,is_save=True).exists()
            food_info = FoodList.objects.filter(id=food_id).first() 
            selected_food_list = {'save_count':save_count,'is_saved':is_saved,'name':food_info.name,'id':food_info.id,'email':email}

            return HttpResponse(json.dumps(selected_food_list), content_type="application/json")
        
# 저장된목록
class SaveList(TemplateView):
    template_name = 'content/savelist.html'

    def get(self,request):
        email = request.session.get('email',None)

        if email == None:     
            email = {'email':email}
            return HttpResponse(json.dumps(email), content_type="application/json")
        
        id_list = Save.objects.filter(email=email,is_save=True).values_list('id', flat=True)
        food_lists = FoodList.objects.filter(id__in=id_list).prefetch_related('memo_set')

        for food_list in food_lists:
            memo_list = []
            for memo in food_list.memo_set.all():
                memo_list.append(memo.memo)
            food_list.memo_list = memo_list

        context = {
            'food_lists': food_lists
        }
        return render(request, 'content/savelist.html', context)
    
    def post(self,request):
        if 'memo_text' in request.POST:
            memo_text = request.POST.get('memo_text', '')
            food_id = request.POST.get('food_id',None)
            email = request.session.get('email',None)
            print(memo_text)

            food = FoodList.objects.get(id=food_id)
            save_memo = Save_memo.objects.filter(food_id=food,email=email).first()

            if save_memo:
                save_memo.memo = memo_text
                save_memo.save()
            else:
                Save_memo.objects.create(food_id=food, memo=memo_text,email=email)

        elif 'save_text' in request.POST:
            food_id = request.POST.get('food_id',None)
            save_text = request.POST.get('save_text',True)
            email = request.session.get('email',None)
            print(save_text)
            if save_text == '저장 취소':
                is_save = False

            save = Save.objects.filter(food_id=food_id,email=email).first()

            if save:
                save.is_save = is_save
                save.save()
            else:
                Save.objects.create(food_id=food_id, is_save=is_save,email=email)
        print(3)
        print(request.POST)
        return render(request, 'content/savelist.html')
