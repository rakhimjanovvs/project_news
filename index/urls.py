from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('register', views.Register.as_view()),
    path('logout', views.logout_view),
    path('login', views.login_view),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('add/', views.add_news, name='add_news'),
    path('category/<int:pk>/', views.news_by_category, name='news_by_category'),
]