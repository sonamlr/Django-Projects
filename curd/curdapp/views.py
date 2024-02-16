from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def add(request):
    return render(request, 'add.html')

def edit(request):
    return render(request, 'edit.html')