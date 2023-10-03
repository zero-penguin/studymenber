from django.urls import path, include
# app全体のviewのインポート
from . import views


urlpatterns = [
    path('',views.Login,name='Login'),
    path('accounts/login',views.Login,name='Login'),
    path("logout",views.Logout,name="Logout"),
    path('register',views.AccountRegistration.as_view(), name='register'),
    path('post', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('comment_delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('post/<int:pk>/change_day/', views.change_day, name='change_day'),
]

