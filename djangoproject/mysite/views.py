from django.http import HttpResponse
from django.shortcuts import render


# life views project

def index(request):
    context = {
        'title':'My Portofolio',
        'hero':'Selamat Data Di Web Portfolio Saya, Terima Kasih!',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/contact','Contact'],
        ],
        'banner':'images/beranda.png'
    }
    return render(request, 'index.html', context)