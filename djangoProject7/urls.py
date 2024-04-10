from django.urls import path
from KR1 import views

urlpatterns = [
    path('', views.first_page),
    path("1/", views.second_page),
    path('2/', views.second_page),
    path('3/', views.thr_page)
]