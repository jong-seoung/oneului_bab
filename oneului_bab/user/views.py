from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib import messages
from user.forms import CustomLoginForm
from .models import User
from django.shortcuts import render, redirect

class LoginView(LoginView):           # 로그인
    authentication_form = CustomLoginForm
    template_name = 'user/login.html'

    def form_invalid(self, form):
        messages.error(self.request, '아이디(로그인 전용 아이디) 또는 비밀번호를 잘못 입력했습니다. \n입력하신 내용을 다시 확인해주세요.', extra_tags='danger')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        # 로그인이 성공하면 리디렉션할 URL
        redirect_to = reverse_lazy('main')

        # 사용자 인증
        user = form.get_user()
        authenticated_user = authenticate(
            username=user.username,
            password=form.cleaned_data.get('password')
        )

        if authenticated_user is not None:
            # 로그인 성공 시 세션에 사용자 정보를 저장합니다.
            login(self.request, authenticated_user)
            return HttpResponseRedirect(redirect_to)

        return super().form_invalid(form)
    
class LogoutView(LogoutView):
    next_page = reverse_lazy('loginview') # 로그아웃 시 리디렉션할 URL

    def get_next_page(self):
        next_page = super().get_next_page()
        messages.success(self.request, '로그아웃되었습니다.', extra_tags='success')
        return self.next_page

class FindIDView(View):
    template_name = 'user/Find_ID.html'
    def get(self, request):
        return render(request, 'user/find_ID.html')
    
class FindPasswordView(View):
    template_name = 'user/Find_Password.html'
    def get(self, request):
        return render(request, 'user/find_Password.html')
    
class JoinView(View):
    template_name = 'user/join.html'
    def get(self, request):
        return render(request, 'user/join.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        name = request.POST['name']
        nickname = request.POST['nickname']
        birthdate_year = request.POST['birthdate_year']
        birthdate_month = request.POST['birthdate_month']
        birthdate_days = request.POST['birthdate_days']
        birthdate = birthdate_year + "-" + birthdate_month + "-" + birthdate_days
        emailcode = request.POST['emailcode']
        info = {'email': email, 'password': password, 'confirm_password': confirm_password, 'name': name, 'nickname': nickname, 'birthdate_year': birthdate_year, 'birthdate_month': birthdate_month, 'birthdate_days': birthdate_days, 'emailcode': emailcode}
        
        if password != confirm_password:
            messages.error(request, '비밀번호와 비밀번호 확인이 일치하지 않습니다.')
            return HttpResponse(render(request, 'user/join.html', info))
        
        if User.objects.filter(email=email).exists():
            messages.error(request, '이미 존재하는 이메일입니다.')
            return HttpResponse(render(request, 'user/join.html', info))
        
        if emailcode == "":
            messages.error(request, '이메일 인증을 해주세요')
            return HttpResponse(render(request, 'user/join.html', info))
        elif emailcode != "o":
            messages.error(request, '인증코드가 올바르지않습니다.')
            return HttpResponse(render(request, 'user/join.html', info))
        
        
        # user = User.objects.create_user(email=email, password=password, name=name, nickname=nickname, birth_date=birthdate)

        # user.save()

        # user = authenticate(email=email, password=password)
        # login(request, user)

        messages.success(request, '회원가입이 완료되었습니다.')
        return redirect('loginview')