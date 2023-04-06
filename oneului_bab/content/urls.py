from django.urls import path
from content.views import Main, Index, recommend, Question_Answer, ToggleSave, SaveList

urlpatterns = [
    path('',Main.as_view(),name="main"),
    path('recommend/',recommend,name="recommendname"),
    path('question/', Question_Answer.as_view(),name="question"),
    path('index/',Index.as_view(),name="index"),
    path('savelist/',SaveList.as_view(),name="savelistveiw"),
    path('save',ToggleSave.as_view()),
]