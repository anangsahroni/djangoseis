from django.urls import path
from . import views

app_name = 'lessons'

urlpatterns = [
    path('', views.lessons_list, name="list"),
    path('create/', views.lesson_create, name="create"),
    path('<str:slug>/', views.lesson_detail, name="detail"),
]
