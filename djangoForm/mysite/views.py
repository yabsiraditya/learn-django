from django.shortcuts import render

def index(request):

    context = {
        'title':'Home',
        'heading':'Django Forms',
    }

    if request.method == 'POST':
        context['nama'] = request.POST['nama']
        context['email'] = request.POST['email']
        context['pesan'] = request.POST['pesan']

    return render(request, 'index.html', context)