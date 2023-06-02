# views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
# Create your views here.

def index(response, id):
	ls = ToDoList.objects.get(id=id)
	return render(response, "main/list.html", {"ls":ls})

def home(response):
	return render(response, "main/home.html", {})

#def create(response):
#   return render(response, "main/create.html", {"form": form}) # goes inside views.py

from .forms import CreateNewList
def create(request):
    form = CreateNewList()
    return render(request, "main/create.html", {"form": form})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()

        #return HttpResponseRedirect("/%i" %t.id)
        return HttpResponseRedirect("/1")

    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form":form})
