from django.urls import path
from .import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('logout_bt/', auth_view.LogoutView.as_view(template_name='users/logout_bt.html'), name="logout_bt"),
    path('statement/', views.statement, name='statement'),  
    path('profile/', views.user_profile, name='user_profile'),  
]
