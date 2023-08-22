from django.urls import path
# app全体のviewのインポート
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

