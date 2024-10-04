from django.shortcuts import render

from .models import Artikel

# Create your views here.
def index(request):
    context = {
        'title':'Blog',
        'headline':'Ini Halaman Blog',
    }
    return render(request, 'index.html', context)


def kategori(request, kategoriInput):
    category = Artikel.objects.filter(kategori=kategoriInput)
    context = {
        'title':'Kategori',
        'headline':'Ini Halaman Artikel Berdasarkan Kategori',
        'categories': category,
    }
    return render(request, 'blog/kategori.html', context)

def detail_artikel(request, slugInput):
    articles = Artikel.objects.get(slug=slugInput)
    context = {
        'title':'Detail Artikel',
        'headline':'Ini Halaman Detail Artikel',
        'articles': articles,
    }
    return render(request, 'blog/detail_artikel.html', context)
