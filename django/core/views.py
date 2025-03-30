from django.shortcuts import render
from .forms import RatingForm, WorkshopForm
from core.models import WorkshopRepair, Sale, Rating, StaffWorkshoprepair
from django.db.models import Sum, Prefetch
from django.utils import timezone
from core.forms import ProductOrderForm

# Create your views here.
def index(request):
    # if request.method == 'POST':
    #     form = WorkshopForm(request.POST or None)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #     else:
    #         return render(request, 'index.html', {'form':form})
    # context = {'form': WorkshopForm()}

    # workshoprepairs = WorkshopRepair.objects.prefetch_related('ratings', 'sales')
    # context = {'workshoprepairs': workshoprepairs}

    # ratings = Rating.objects.only('rating', 'workshoprepair__name').select_related('workshoprepair')

    # month_ago = timezone.now() - timezone.timedelta(days=30)
    # monthly_sales = Prefetch(
    #         'sales',
    #         queryset=Sale.objects.filter(datetime__gte=month_ago)
    #     )
    # workshoprepair = WorkshopRepair.objects.prefetch_related('ratings', monthly_sales).filter(ratings__rating=5)
    # workshoprepair = workshoprepair.annotate(total=Sum('sales__income'))
    # # context = {'workshoprepairs': workshoprepair}
    # print([r.total for r in workshoprepair])

    jobs = StaffWorkshoprepair.objects.prefetch_related('staff', 'workshoprepair')

    for job in jobs:
        print(job.workshoprepair.name)
        print(job.staff.name)

    return render(request, 'index.html')


def order_product(request):
    form = ProductOrderForm
    context = {
        'form':form
    }

    return render(request, 'order.html', context)