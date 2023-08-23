from django.urls import path
# app全体のviewのインポート
from . import views

app_name = "blog"
urlpatterns = [
    # 一覧
    path("", views.ProductListView.as_view(), name="list"),
]