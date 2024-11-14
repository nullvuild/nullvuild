from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# [nullvuild] add app_name
app_name = 'user'

urlpatterns = [
    path('', views.index, name='index'),  # 기본 URL
    path('signup/', views.signup, name='signup'), #추가
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]