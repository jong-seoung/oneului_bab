from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib import messages
from user.forms import CustomLoginForm
from .models import User
from django.shortcuts import render, HttpResponseRedirect
import smtplib
from email.mime.text import MIMEText

#########################
import json
import os
import smtplib
from email.mime.text import MIMEText

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
secrets_file = os.path.join(BASE_DIR, 'secrets.json')
##########################

class LoginView(LoginView):           # 로그인
    authentication_form = CustomLoginForm
    template_name = 'user/login.html'

    def form_invalid(self, form):
        messages.error(self.request, '아이디(로그인 전용 아이디) 또는 비밀번호를 잘못 입력했습니다. \n입력하신 내용을 다시 확인해주세요.', extra_tags='danger')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        redirect_to = reverse_lazy('main')

        user = form.get_user()
        authenticated_user = authenticate(
            username=user.email,
            password=form.cleaned_data.get('password')
        )

        if authenticated_user is not None:
            login(self.request, authenticated_user)
            return HttpResponseRedirect(redirect_to)

        return super().form_invalid(form)
    
class LogoutView(LogoutView):
    next_page = reverse_lazy('loginview')

    def get_next_page(self):
        next_page = super().get_next_page()
        messages.success(self.request, '로그아웃되었습니다.', extra_tags='success')
        return self.next_page

class FindIDView(View):
    template_name = 'user/find_ID.html'
    def get(self, request):
        return render(request, 'user/find_ID.html')
    
    def post(self, request):
        email = request.POST['email']
        name = request.POST['name']
        birthdate_year = request.POST['birthdate_year']
        birthdate_month = request.POST['birthdate_month']
        birthdate_days = request.POST['birthdate_days']
        birthdate = birthdate_year + "-" + birthdate_month + "-" + birthdate_days
        info = {'email': email,'name': name,'birthdate_year': birthdate_year, 'birthdate_month': birthdate_month, 'birthdate_days': birthdate_days}

        try:
            user = User.objects.get(email=email, name=name, birth_date=birthdate)
            if str(user) == email:
                messages.info(request, '회원 정보가 일치합니다.')
            else:
                messages.error(request, '회원정보가 없거나 잘못되었습니다.')
                return render(request, 'user/find_ID.html', info)
        except:
            messages.error(request, '회원정보가 없거나 잘못되었습니다.')
            return render(request, 'user/find_ID.html', info)

        return HttpResponse(render(request, 'user/find_ID.html', info))
    
class FindPasswordView(View):
    template_name = 'user/find_Password.html'
    def get(self, request):
        return render(request, 'user/find_Password.html')
    
class JoinView(View):
    template_name = 'user/join.html'
    def get(self, request):
        return render(request, 'user/join.html')

    def send_email_code(self, request, email):
        import random
        code = random.randint(100000, 999999)
        message = f"이메일 인증 코드 입니다. : {code}"
        msg = MIMEText(message)
        msg['Subject'] = '오늘의 밥 : 회원가입 인증 코드'
        msg['From'] = 'jjong015189@gmail.com'
        msg['To'] = email

        with open(secrets_file) as f:
            secrets = json.load(f)

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('jjong015189@gmail.com', secrets['GMAIL_KEY'])
        s.sendmail('jjong015189@gmail.com', [email], msg.as_string())
        s.quit()
        request.session['email_verification_code'] = code
        return code

    def check_email_code(self, request):
        emailcode = request.POST['emailcode']
        if 'email_verification_code' in request.session:
            if int(emailcode) == request.session['email_verification_code']:
                return True
        return False
    
    def post(self, request):
        if request.POST.get('submit') == 'email-verify':
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
            
            if User.objects.filter(nickname=nickname).exists():
                messages.error(request, '이미 존재하는 닉네임입니다.')
                return HttpResponse(render(request, 'user/join.html', info))

            self.send_email_code(request, email)
            
            messages.success(request, '인증번호가 전송되었습니다.')
            return HttpResponse(render(request, 'user/join.html', info))
        elif request.POST.get('submit') == 'join':
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
            
            if User.objects.filter(nickname=nickname).exists():
                messages.error(request, '이미 존재하는 닉네임입니다.')
                return HttpResponse(render(request, 'user/join.html', info))
            
            if emailcode == "":
                messages.error(request, '이메일 인증을 해주세요')
                return HttpResponse(render(request, 'user/join.html', info))
            else:
                if self.check_email_code(request) == True:
                    messages.success(request, '회원가입이 완료되었습니다.')
                    user = User.objects.create_user(email=email, password=password, name=name, nickname=nickname, birth_date=birthdate,is_active=True)
                    user.save()
                    user = authenticate(email=email, password=password)
                    login(request, user)
                elif self.check_email_code(request) == False:
                    messages.success(request, '인증번호가 잘못되었습니다. 다시 확인해주세요.')
                    return HttpResponse(render(request, 'user/join.html', info))
        return redirect('loginview')
