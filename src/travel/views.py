
from django.shortcuts import render

def home(request):
    name = 'Bob'
    
    return render(request, 'home.html', {'name': name})

def about(request):
    are = 54
    return render(request, 'about.html', {'are': are})