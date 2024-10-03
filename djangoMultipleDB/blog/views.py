from django.shortcuts import render

from .models import Artikel

# Create your views here.
def index(request):
    semuaArtikel = Artikel.objects.using('db_blog').order_by('judul')
    print(semuaArtikel)
    context = {
        'title':'Blog',
        'headline':'Selamat Datang di Halaman Blog',
        'articles':semuaArtikel,
    }
    return render(request, 'index.html', context)


def stoping(request):
    semuaArtikel = Artikel.objects.using('db_blog').filter(pilih_kategori__nama='Stoping')
    print(semuaArtikel)
    context = {
        'title':'Blog',
        'headline':'Selamat Datang di Halaman Blog Stoping',
        'articles':semuaArtikel,
    }
    return render(request, 'index.html', context)


def peduli(request):
    semuaArtikel = Artikel.objects.using('db_blog').filter(pilih_kategori__nama='Peduli')
    print(semuaArtikel)
    context = {
        'title':'Blog',
        'headline':'Selamat Datang di Halaman Blog Peduli',
        'articles':semuaArtikel,
    }
    return render(request, 'index.html', context)


def viral(request):
    semuaArtikel = Artikel.objects.using('db_blog').filter(pilih_kategori__nama='Viral')
    print(semuaArtikel)
    context = {
        'title':'Blog',
        'headline':'Selamat Datang di Halaman Blog Viral',
        'articles':semuaArtikel,
    }
    return render(request, 'index.html', context)


def berita(request):
    semuaArtikel = Artikel.objects.using('db_blog').filter(pilih_kategori__nama='Berita')
    print(semuaArtikel)
    context = {
        'title':'Blog',
        'headline':'Selamat Datang di Halaman Blog Berita',
        'articles':semuaArtikel,
    }
    return render(request, 'index.html', context)