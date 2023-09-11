from django.urls import path, include
# app全体のviewのインポート
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', include('django_summernote.urls'),views.post_detail, name='post_detail'),
]

