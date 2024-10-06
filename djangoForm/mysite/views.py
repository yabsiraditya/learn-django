from django.shortcuts import render

from .forms import FormsFields

def index(request):
    form_fields = FormsFields()

    context = {
        'title':'Home',
        'heading':'Django Forms',
        'form_fields': form_fields,
    }

    return render(request, 'index.html', context)