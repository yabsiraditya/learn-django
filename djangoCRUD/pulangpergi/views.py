from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib import messages

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
    messages.success(request, 'Data berhasil dihapus')
    return redirect('pulangpergi:index')

def update(request, nameSlug):
    # objDestination = Destination.objects.get(slug=nameSlug)

    objDestination = get_object_or_404(Destination, slug=nameSlug)

    if request.method == 'POST':
        form = DestinationForm(request.POST or None, request.FILES or None, instance=objDestination)
        if form.is_valid():
            form.save()
            messages.warning(request, 'Data berhasil diupdate')
            return redirect('pulangpergi:index')
    else:
        form = DestinationForm(instance=objDestination)

    context = {
        'title':'Halaman PulangPergi',
        'heading':'Edit Tujuan PulangPergi',
        'form':form,
    }

    return render(request, 'update.html', context)

def addDestination(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data berhasil ditambahkan')
            return redirect('pulangpergi:index')
    else:
        form = DestinationForm()

    context = {
        'title':'Halaman PulangPergi',
        'heading':'Tambah Tujuan PulangPergi',
        'form':form,
    }

    return render(request, 'create.html', context)