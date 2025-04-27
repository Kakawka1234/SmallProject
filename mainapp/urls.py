from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_task, name='create_task'),
    path('tasks/', views.task_list, name='task_list'),
    path('task/<int:task_id>/change_status/', views.change_status, name='change_status')
]