from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'Halaman Home PulangPergi',
        'heading':'Selamat Datang Di PulangPergi',
    }

    return render(request, 'index.html', context)