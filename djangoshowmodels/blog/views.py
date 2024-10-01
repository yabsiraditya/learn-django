from django.shortcuts import render

# Create your views here.
from .models import Artikel

def index(request):
    # Queryset
    allArtikel = Artikel.objects.all()
    context = {
        'title':'blog',
        'headline':'halaman blog',
        'semuaArtikel':allArtikel,
    }
    return render(request, 'index.html', context)