from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

def home(request):
    user = User.objects.all()
    return render(request, 'base.html', {'users':user})

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return redirect('/')
        else:
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    
    return render(request, 'add.html',{'form': fm})
    
    



def update_data(request):
    return render(request, 'edit.html')

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('/')