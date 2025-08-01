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