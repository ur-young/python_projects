
from django.urls import path , include
from recommend_app import views

urlpatterns = [
    path('', views.index),
    path('read/<id>/',views.read),
    path('recommend/',views.recommend),
    path('show/',views.show),
    path('data/',views.data),
    path('write/',views.write),# 이거 지우기
    path('read_post/<id>/',views.read_post),
]
