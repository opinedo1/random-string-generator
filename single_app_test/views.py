from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

#redirects back to "/" directory with method below
def create(request):
    return redirect('/')

#shows the integer value that is found in the url
def show(request, val):
    return HttpResponse("placeholder to display blog number {}".format(val))

def edit(request, number):
    return HttpResponse("placeholder to edit blog {}".format(number))

def destroy(request, number):
    return redirect('/')