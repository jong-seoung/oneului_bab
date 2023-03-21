from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from user.forms import CustomLoginForm

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