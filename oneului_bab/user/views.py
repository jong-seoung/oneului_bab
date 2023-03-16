from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView

class Login(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse('main')