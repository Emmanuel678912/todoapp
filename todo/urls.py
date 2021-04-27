from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name="register"),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('delete', views.delete_task, name='delete'),
    path('tasks', views.tasks, name='tasks'),
        
]
