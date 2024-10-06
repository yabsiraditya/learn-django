from django.shortcuts import render

from .forms import KontakForms
# Create your views here.
def index(request):
    kontak_forms = KontakForms()

    context = {
        'title':'Kontak',
        'heading':'Kontak Forms',
        'kontak_forms': kontak_forms,
    }

    if request.method == 'POST':
        context['nama'] = request.POST['nama']
        context['email'] = request.POST['email']
        context['no_telp'] = request.POST['no_telp']
        context['tgl_lahir'] = request.POST['tgl_lahir_day']
        context['tgl_lahir'] = request.POST['tgl_lahir_month']
        context['tgl_lahir'] = request.POST['tgl_lahir_year']
        context['jenkel'] = request.POST['jenkel']
        context['subjek'] = request.POST['subjek']
        context['pesan'] = request.POST['pesan']
        context['alamat'] = request.POST['alamat']

    return render(request, 'kontak.html', context)