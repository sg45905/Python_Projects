from django.urls import path
from .views import index, addTodo, completeTodo, deletecompleted, deleteall

urlpatterns = [
    path('', index, name='index'),
    path('add', addTodo, name='add'),
    path('complete/<todo_id>', completeTodo, name='complete'),
    path('deletecomplete', deletecompleted, name='deletecomplete'),
    path('deleteall', deleteall, name='deleteall')
]
