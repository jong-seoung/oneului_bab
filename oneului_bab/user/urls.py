from django.urls import path
from user.views import LoginView, LogoutView, FindIDView, FindPasswordView, JoinView, ChangePasswordView, UserInfoeView

urlpatterns = [
    path('login/',LoginView.as_view(),name="loginview"),
    path('logout/',LogoutView.as_view(),name="logoutview"),
    path('join/',JoinView.as_view(),name="joinview"),
    path('findid/',FindIDView.as_view(),name="findidview"),
    path('findpassword/',FindPasswordView.as_view(),name="findpasswordview"),
    path('changepassword/<str:emailcode>/', ChangePasswordView.as_view(), name='changepasswordview'),
    path('<int:pk>/update/', UserInfoeView.update, name='update'),
    path('<int:pk>/changepassword/', UserInfoeView.chagepassword, name='changepassword'),
    path('<int:pk>/', UserInfoeView.detail, name='detail'),
]