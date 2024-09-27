from django.http import HttpResponse
from django.shortcuts import render


# life views project

def index(request):
    context = {
        'title':'Web Developer',
        'hero':'Web Developer Full Stack',
        'developer':'Yabsir Aditya'
    }
    return render(request, 'index.html', context)