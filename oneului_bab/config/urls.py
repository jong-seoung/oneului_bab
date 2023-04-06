"""oneului_bab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from user.views import Login
from content.views import Main, Index, recommend, Question_Answer, ToggleSave, SaveList
from user.views import LoginView, LogoutView, FindIDView, FindPasswordView, JoinView, ChangePasswordView, UserInfoeView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Main.as_view(),name="main"),
    path('recommend/',recommend,name="recommendname"),
    path('question/', Question_Answer.as_view(),name="question"),
    path('index/',Index.as_view(),name="index"),
    path('savelist/',SaveList.as_view(),name="savelistveiw"),
    path('save',ToggleSave.as_view()),

    path('login/',LoginView.as_view(),name="loginview"),
    path('logout/',LogoutView.as_view(),name="logoutview"),
    path('join/',JoinView.as_view(),name="joinview"),
    path('findid/',FindIDView.as_view(),name="findidview"),
    path('findpassword/',FindPasswordView.as_view(),name="findpasswordview"),
    path('changepassword/<str:emailcode>/', ChangePasswordView.as_view(), name='changepasswordview'),
    path('<int:pk>/update/', UserInfoeView.update, name='update'),
    path('<int:pk>/', UserInfoeView.detail, name='detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
