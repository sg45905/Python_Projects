from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import NewTodoForm

def index(request):
	todo_list = Todo.objects.order_by('id')
	newtodoform = NewTodoForm()

	context = {'todo_list': todo_list, 'form': newtodoform}
	
	return render(request, 'index.html', context)

@require_POST
def addTodo(request):
	newtodoform = NewTodoForm(request.POST)
	
	if newtodoform.is_valid():
		new_todo = newtodoform.save()
	
	return redirect('index')

def completeTodo(request,todo_id):
	todo = Todo.objects.get(pk=todo_id)
	todo.complete = True
	todo.save()

	return redirect('index')

def deletecompleted(request):
	Todo.objects.filter(complete__exact=True).delete()

	return redirect('index')

def deleteall(request):
	Todo.objects.all().delete()

	return redirect('index')
