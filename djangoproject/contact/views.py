from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'title':'Contact Saya',
        'hero':'Ini Adalah Halaman Contact Saya',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/contact','Contact'],
        ],
        'banner':'contact/images/kontak.png',
        'css_apps':'contact/css/style_contact.css'
    }
    return render(request, 'index.html', context)
