from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.get_students, name='get_students'),
    path('tasks/', views.get_tasks, name='get_tasks'),
]