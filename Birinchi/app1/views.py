from django.shortcuts import render, redirect
from django.http import *
from .models import *

def salom(request):
    data={
        'Muallif': Muallif.objects.all()
    }
    return render(request,'Muallif.html',data)

def key(request,son):
    data={
        'Muallif2': Muallif.objects.filter(id=son)
    }
    return render(request,'task2.html',data)

def kitob(request):
    data={
        'Kitob': Kitob.objects.all()
    }
    return render(request,'Kitob.html',data)
def kitob2(request,a):
    data={
        'kitob': Kitob.objects.filter(id=a)
    }
    return render(request,'task-4.html',data)

def record(request):
    data={
        'record': Record.objects.all()
    }
    return render(request,'Record.html',data)
def Tmuallif(request):
    data={
        'tirik': Muallif.objects.filter(trik=True)
    }
    return render(request,'tirik.html',data)
def bkitob(request):
    data={
        'Bkitob': Kitob.objects.filter(janr='badiiy')
    }
    return render(request,'Kitob.html',data)













def Talaba(request,son):
    data={
        'talaba':Oquvchi.objects.all()
    }
    return render(request,'Talabalar.html',data)
def ochir(request,son):
    Oquvchi.objects.filter(id=son).delete()
    return redirect('/Talaba')