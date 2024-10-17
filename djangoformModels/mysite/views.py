from django.shortcuts import render

def index(request):
    context = {
        'title':'Halaman Home',
        'heading':'Selamat Datang Di Home',
    }

    return render(request, 'index.html', context)