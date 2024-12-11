from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todoapp

# Create your views here.
def todo_list(request):
    all_data = {'todo_list':todoapp.objects.all()}
    return render(request, "OTtodo/todo_list.html", all_data)

def insert_todo(request:HttpResponse):
    Todo = todoapp(content = request.POST ['content'])
    Todo.save()
    return redirect('/list') 

def delete_todo_item(request, todo_id):
    delete_id = todoapp.objects.get(id=todo_id)
    delete_id.delete()
    return redirect('/list')


