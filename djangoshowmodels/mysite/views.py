from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title':'home',
        'headline':'halaman home',
    }
    return render(request, 'index.html', context)