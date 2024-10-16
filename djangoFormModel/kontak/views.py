from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import KontakForm
from .models import KontakModel as Kontak

def index(request):
    contacts = Kontak.objects.all().order_by('-dateTime')
    context = {
        'title':'Halaman Kontak',
        'heading':'Daftar Kontak Masuk',
        'contacts': contacts,
    }

    return render(request, 'kontak.html', context)


def create(request):
    f_kontak = KontakForm(request.POST or None)
    salah = None

    if request.method == 'POST':
        if f_kontak.is_valid():
            Kontak.objects.create(
                name = f_kontak.cleaned_data.get('name'),
                email = f_kontak.cleaned_data.get('email'),
                message = f_kontak.cleaned_data.get('message'),
            )
            return HttpResponseRedirect('/kontak/')
        else:
            salah = f_kontak.errors

    context = {
        'title':'Kirim Pesan',
        'heading':'Kirim Pesan',
        'f_kontak':f_kontak,
        'salah':salah,
    }

    return render(request, 'create.html', context)