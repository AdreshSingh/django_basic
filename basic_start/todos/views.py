from django.shortcuts import render
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect

from .models import Todos
from .form import TodosForm

# Create your views here.

# search homepage
def home(request):
    #? fetching data from SQLite
    todos = Todos.objects.all()
    print(todos)
    #? storing
    context={
        "data":todos
    }
    return render(request,'home.html',context=context)

def addtodos(request):
    if request.method == "POST":
        form = TodosForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    else:
        form = TodosForm()
        
        return render(request,'newtodo.html',context={"form":form})


def detail(request,id):
    todo = Todos.objects.get(id=id) #! ID is always unique

    context = {
        "todo":todo
    }

    return render(request,"detail.html",context)

def deletetodo(request,id):
    todo_remove = Todos.objects.get(id=id)
    todo_remove.delete()

    #? fetching data from SQLite
    todos = Todos.objects.all()
   
    #? storing
    context={
        "data":todos
    }
    return render(request,'home.html',context=context)

def updatetodo(request,id):
    todo = Todos.objects.get(id=id)
    if request.method == "POST":
        form = TodosForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
    else:
        form=TodosForm(instance=todo)
    
    return render(request,"update.html",{"form":form,"todo":todo})
    