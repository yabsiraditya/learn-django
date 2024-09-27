from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# def about(request):
#     return HttpResponse("<h1>Ini Adalah Halaman about</h1>")