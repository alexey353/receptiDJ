from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main\index.html')

def about(request):
    return render(request, 'main/about.html')

def catalog(request):
    return render(request, 'main\catalog.html')

def contact(request):
    return render(request, 'main/contact.html')