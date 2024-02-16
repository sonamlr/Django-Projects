from django.shortcuts import render
from service.models import Todo
def home(request):
    todo_list = Todo.objects.all()
    data = {'todolist':todo_list}
    return render(request, 'home.html',data)