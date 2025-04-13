from django.shortcuts import render, redirect, get_object_or_404
from .forms import RatingForm, WorkshopForm
from core.models import WorkshopRepair, Sale, Rating, StaffWorkshoprepair, Product
from django.db.models import Sum, Prefetch
from django.db import transaction
from django.utils import timezone
from core.forms import ProductOrderForm
from functools import partial


def email_user(email):
    print(f"Dear {email}, Thank you for your order")


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

    # jobs = StaffWorkshoprepair.objects.prefetch_related('staff', 'workshoprepair')

    # for job in jobs:
    #     print(job.workshoprepair.name)
    #     print(job.staff.name)

    context = {
        'workshoprepairs':WorkshopRepair.objects.all()[:5]
    }

    return render(request, 'index.html', context)


def order_product(request):
    if request.method == 'POST':
        form = ProductOrderForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                product = Product.objects.select_for_update().get(
                    id=form.cleaned_data['product'].pk
                )
                import time
                time.sleep(85)
                order = form.save()
                order.product.number_in_stock -= order.number_of_items
                order.product.save()
            transaction.on_commit(partial(email_user, "admin@test.com"))

            return redirect('order-product')
        else:
            context = {
                'form':form
            }
            return render(request, 'order.html', context)

    form = ProductOrderForm()
    context = {
        'form':form
    }

    return render(request, 'order.html', context)

def workshoprepair_detail(request, pk):
    workshoprepair = get_object_or_404(WorkshopRepair, pk=pk)
    return render(request, 'workshoprepair.html', {'workshoprepair':workshoprepair})