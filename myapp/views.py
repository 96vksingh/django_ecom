from django.shortcuts import render,HttpResponse
from .models import Todoitem
# Create your views here.
def home(request):
    return render(request, "home.html")

def todo(request):
    items = Todoitem.objects.all()
    return render(request, "todo.html",{"todos":items})