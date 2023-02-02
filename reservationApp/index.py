from django.http import HttpResponse
from django.shortcuts import render

def recuperation(request):
    return render(request,'recuperation.html')

def dashbord(request):
    return render(request, 'dashbord.html')

def connection(request):
    return render(request,'connection.html')

def code(request):
    return render(request,'code_recuperation.html')