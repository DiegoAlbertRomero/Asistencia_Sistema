from django.urls import path
from generales.views import home, login, logout, reportes 
from . import views

urlpatterns = [
    path('', home, name = 'home'),
    path('login/', login, name='login'),
    path('logout/', logout, name = 'logout'),
    path('reportes/', reportes,  name = 'reportes'),
    path('login/', views.login_view, name='login'),
    path('', views.home_view, name='home'),
    
]
