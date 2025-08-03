from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('register', views.Register.as_view()),
]