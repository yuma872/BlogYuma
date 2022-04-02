from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title': 'Блог Юмы'
    }
    return render(request, 'main/index.html', data)

def contacts(request):
    return render(request, 'main/contacts.html')
