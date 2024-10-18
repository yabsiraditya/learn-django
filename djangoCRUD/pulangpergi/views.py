from django.shortcuts import render, redirect

# import models
from .models import Destination

# import forms
from .forms import DestinationForm


# Create your views here.
def index(request):
    allDestination = Destination.objects.all()
    context = {
        'title':'Halaman PulangPergi',
        'heading':'Pesanan PulangPergi',
        'allDestination':allDestination,
    }

    return render(request, 'pulangpergi.html', context)

def delete(request, nameSlug):
    Destination.objects.filter(slug=nameSlug).delete()
    return redirect('pulangpergi:index')

def addDestination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('pulangpergi:index')
    else:
        form = DestinationForm()

    context = {
        'title':'Halaman PulangPergi',
        'heading':'Tambah Tujuan PulangPergi',
        'form':form,
    }

    return render(request, 'create.html', context)