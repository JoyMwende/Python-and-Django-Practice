from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello!")
    return render(request, "hello/index.html") # render a template

def brian(request):
    return HttpResponse("Hello, Brian!") # return a string

def david(request):
    return HttpResponse("Hello, David!")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    # context: all additional information I would like to provide for the template
    return render(request, "hello/greet.html", {
        "name": name.capitalize() # pass the name to the template
    })