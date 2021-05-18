from . import views
from django.urls import path

urlpatterns = [
    path('', views.display, name='display'),
    path('signup/', views.register, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
