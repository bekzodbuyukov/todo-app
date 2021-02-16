from django.urls import path
from .views import TodoDetail, TodoList


urlpatterns = [
    path('todos/', TodoList.as_view(), name='todo_list'),
    path('todos/<int:todo_id>', TodoDetail.as_view(), name='todo_detail')
]