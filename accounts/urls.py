from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.registerPage, name="register_page"),
	path('login/', views.loginPage, name="login_page"),  
	path('logout/', views.logoutUser, name="logout_page"),
]