from django.shortcuts import render
from .forms import RatingForm, WorkshopForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = WorkshopForm(request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
        else:
            return render(request, 'index.html', {'form':form})
    context = {'form': WorkshopForm()}
    return render(request, 'index.html', context)