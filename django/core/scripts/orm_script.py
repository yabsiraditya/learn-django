from core.models import WorkshopRepair, User, Rating, Sale, Staff, StaffWorkshoprepair
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower, Upper, Length, Concat
from django.db.models import Count, Avg, Min, Max, Sum, StdDev, Variance, CharField, Value, F, Q
import random

def run():
    
    # workshoprepair = WorkshopRepair()
    # workshoprepair.name = 'Astra Honda Cibinong'
    # workshoprepair.latitude = -6.471236
    # workshoprepair.longitude = 106.861915
    # workshoprepair.date_opened = timezone.now()
    # workshoprepair.workshop_type = WorkshopRepair.TypeWorkshop.MOTORCYCLE
    
    # workshoprepair.save()

    # workshoprepair = WorkshopRepair.objects.all()
    # print(workshoprepair)

    # WorkshopRepair.objects.create(
    #     name="Yamaha Arista Citeureup",
    #     date_opened=timezone.now(),
    #     workshop_type = WorkshopRepair.TypeWorkshop.MOTORCYCLE,
    #     latitude = -6.481179, 
    #     longitude = 106.869037,
    # )
    # print(connection.queries)

    # workshoprepair = WorkshopRepair.objects.first()
    # user = User.objects.first()

    # Rating.objects.create(
    #     user=user,
    #     workshoprepair=workshoprepair,
    #     rating=4,
    # )

    # print(Rating.objects.exclude(rating__lte=3))

    # workshoprepair = WorkshopRepair.objects.first()
    # print(workshoprepair.name)

    # workshoprepair.name = "Astra Honda Motor Cibinong"
    # workshoprepair.save()

    # rating = Rating.objects.first()
    # print(rating.workshoprepair.name)

    # workshoprepair = WorkshopRepair.objects.first()
    # print(workshoprepair.sales.all())

    # Sale.objects.create(
    #     workshoprepair=WorkshopRepair.objects.first(),
    #     income=1.33,
    #     datetime=timezone.now(),
    # )

    # user = User.objects.first()
    # workshoprepair = WorkshopRepair.objects.first()

    # rating = Rating(
    #     user=user,
    #     workshoprepair=workshoprepair,
    #     rating=9,
    # )

    # rating.full_clean()
    # rating.save()

    # rating, created = Rating.objects.get_or_create(
    #     workshoprepair=workshoprepair,
    #     user=user,
    #     rating=3,
    # )

    # if created:
    #     # send email
    #     pass
    
    # workshoprepair = WorkshopRepair.objects.first()
    # print(workshoprepair.name)

    # workshoprepair.name = 'Astra Honda Motor Cibinong'
    # workshoprepair.save()

    # workshoprepair = WorkshopRepair()
    # workshoprepair.name = 'Astra Honda Motor Cibinong #2'
    # workshoprepair.date_opened = timezone.now()
    # workshoprepair.workshop_type = WorkshopRepair.TypeWorkshop.MOTORCYCLE
    # workshoprepair.latitude = 50.2
    # workshoprepair.longitude= 50.2
    # workshoprepair.save()

    # workshoprepair = WorkshopRepair.objects.filter(name__startswith='A')
    # print(workshoprepair)

    # print(workshoprepair.update(
    #     date_opened=timezone.now() - timezone.timedelta(days=365),
    #     website='https://github.com/yabsiraditya'
    # ))

    # workshoprepair = WorkshopRepair.objects.first()
    # print(workshoprepair.delete())


    # WorkshopRepair.objects.all().delete()

    # print(WorkshopRepair.objects.count())
    # print(Rating.objects.count())
    # print(Sale.objects.count())

    # filter car WorkshopRepair

    # workshoprepair = WorkshopRepair.objects.filter(workshop_type=WorkshopRepair.TypeWorkshop.CAR)
    # workshoprepair = WorkshopRepair.objects.filter(name='ajskdhjkashjksd')
    # workshoprepair = WorkshopRepair.objects.filter(name__contains='astra')
    # print(workshoprepair)
    # print(workshoprepair.exists())
    # print(workshoprepair.get())

    # motorcycle = WorkshopRepair.TypeWorkshop.MOTORCYCLE
    # workshoprepair = WorkshopRepair.objects.filter(workshop_type=motorcycle, name__startswith='A')
    # car = WorkshopRepair.TypeWorkshop.CAR
    # bustruck = WorkshopRepair.TypeWorkshop.BUSTRUCK
    # check_types = [car, bustruck]
    # workshoprepair = WorkshopRepair.objects.filter(workshop_type__in=check_types)

    # workshoprepair = WorkshopRepair.objects.exclude(workshop_type__in=[motorcycle, car])
    # workshoprepair = WorkshopRepair.objects.filter(name__lt='R')
    # workshoprepair = WorkshopRepair.objects.filter(name__gt='R')

    # sales = Sale.objects.filter(income__range=(50, 60))
    # print([sale.income for sale in sales])

    # workshoprepair = WorkshopRepair.objects.order_by('name')
    # workshoprepair = WorkshopRepair.objects.order_by('-name') #Reverse
    # sales = Sale.objects.order_by('-datetime')

    # workshoprepair = WorkshopRepair.objects.order_by('date_opened')[2:5]
    # workshoprepair = WorkshopRepair.objects.latest()

    # Find all rating associated with a workshoprepair begining with 'A'.
    # ratings = Rating.objects.filter(workshoprepair__name__startswith='A')

    # car = WorkshopRepair.TypeWorkshop.CAR
    # sales = Sale.objects.filter(workshoprepair__workshop_type=car)

    # print(sales)

    # pprint(connection.queries)


    # staff, created = Staff.objects.get_or_create(
    #     name='John Dhoe'
    # )

    # staff.workshoprepairs.set(
    #     WorkshopRepair.objects.all()[:5],
    #     through_defaults={'salary':random.randint(20_000, 80_000)}
    # )

    # workshoprepair = WorkshopRepair.objects.first()

    # staff.workshoprepairs.add(workshoprepair, through_defaults={'salary': 28_000})

    # StaffWorkshoprepair.objects.create(
    #     staff=staff,
    #     workshoprepair=workshoprepair,
    #     salary=28_000
    # )

    # StaffWorkshoprepair.objects.create(
    #     staff=staff,
    #     workshoprepair=workshoprepair2,
    #     salary=24_000
    # )

    # staff_workshoprepair = StaffWorkshoprepair.objects.filter(staff=staff)

    # for w in staff_workshoprepair:
    #     print(w.salary)

    # print(staff.workshoprepairs.all())
    # add, all, count, remove, set, claer, create, filter
    # staff.workshoprepairs.set(WorkshopRepair.objects.all()[:5])
    # staff.workshoprepairs.clear()
    # car = staff.workshoprepairs.filter(workshop_type=WorkshopRepair.TypeWorkshop.CAR)
    # print(car)
    # print(staff.workshoprepairs.count())

    # workshoprepair = WorkshopRepair.objects.get(pk=10)

    # print(workshoprepair.staff_set.all())

    # workshoprepair = WorkshopRepair.objects.values(name_upper=Upper('name'))[:3]
    
    # BT = WorkshopRepair.TypeWorkshop.BUSTRUCK
    # rating = Rating.objects.filter(workshoprepair__workshop_type=BT).values('rating', 'workshoprepair__name')

    # workshoprepairs = WorkshopRepair.objects.values_list('name', flat=True)

    # one_month_ago = timezone.now() - timezone.timedelta(days=31)

    # print(WorkshopRepair.objects.aggregate(total=Count('id')))
    # print(Rating.objects.filter(workshoprepair__name__startswith='H').aggregate(avg=Avg('rating')))
    # print(Sale.objects.filter(datetime__gte=one_month_ago).aggregate(
    #     min=Min('income'),
    #     max=Max('income'),
    #     avg=Avg('income'),
    #     sum=Sum('income'),
    #     )
    # )

    # fetch all workshoprepair, and let's assume we want 
    # to get the number of characters in the name of the workshoprepair. so 'xyz' == 3.

    # workshoprepair = WorkshopRepair.objects.annotate(len_name=Length('name')).filter(
    #     len_name__gte=30
    # )
    # print(workshoprepair.values('name', 'len_name'))

    # Workshoprepair 1 [Rating : 3.1]
    # conncatenation = Concat(
    #     'name', Value(' [Rating: '), Avg('ratings__rating'), Value(']'),
    #     output_field=CharField()
    # )

    # workshoprepair = WorkshopRepair.objects.annotate(message=conncatenation)
    # for w in workshoprepair:
    #     print(w.message)

    # workshoprepair = WorkshopRepair.objects.annotate(total_sales=Sum('sales__income')).values(
    #     'name', 'total_sales'
    # )
    # print([w['total_sales'] for w in workshoprepair])

    # workshoprepair = WorkshopRepair.objects.annotate(
    #     num_ratings=Count('ratings'),
    #     avg_rating=Avg('ratings__rating')
    # )
    # print(workshoprepair.values('name', 'num_ratings', 'avg_rating'))

    # workshoprepair = WorkshopRepair.objects.values('workshop_type').annotate(
    #     num_ratings=Count('ratings'),
    # )

    # workshoprepair = WorkshopRepair.objects.annotate(total_sales=Sum('sales__income')).order_by('total_sales')
    # workshoprepair = WorkshopRepair.objects.annotate(total_sales=Sum('sales__income')).filter(total_sales__lte=500)
    # print(workshoprepair.aggregate(av_sales=Avg('total_sales')))
    # for r in workshoprepair:
    #     print(f'{r.name} = {r.total_sales}')

    # print(workshoprepair)

    # rating = Rating.objects.filter(rating=3).first()
    # Rating.objects.update(rating=F('rating') / 2)
    # update this rating by 1
    # rating.rating = F('rating') + 1
    # rating.save()
    # sales = Sale.objects.all()

    # for sale in sales:
    #     sale.expenditure = random.uniform(5, 100)

    # Sale.objects.bulk_update(sales, ['expenditure'])

    # sales = Sale.objects.filter(expenditure__gt=F('income'))
    # sales = Sale.objects.annotate(
    #     profit= F('income') - F('expenditure')
    # ).order_by('-profit')
    # sales = Sale.objects.aggregate(
    #     profit=Count('id', filter=Q(income__gt=F('expenditure'))),
    #     loss=Count('id', filter=Q(income__lt=F('expenditure'))),
    # )
    # print(sales)

    # rating = Rating.objects.first()
    # print(rating.rating)
    # rating.rating = F('rating') + 2
    # rating.save()

    # rating.refresh_from_db()

    # print(rating.rating)

    # get all Motorcycle and Car workshop
    # mc=WorkshopRepair.TypeWorkshop.MOTORCYCLE
    # bt=WorkshopRepair.TypeWorkshop.BUSTRUCK

    # print(WorkshopRepair.objects.filter(
    #     Q(workshop_type=mc) | Q(workshop_type=bt)
    # ))

    # find workshoprepair that have the number 1 in the name:
    # icontains, endswith, startswith
    # print(
    #     WorkshopRepair.objects.filter(name__startswith="H")
    # )

    # workshoprepair name contains either the word "Motorcycle" OR the word "Bus Truck"
    # hi_or_ho = Q(name__icontains="Hino") | Q(name__icontains="Honda")
    # recently_opened = Q(date_opened__gt=timezone.now() - timezone.timedelta(days=40))
    # not_recently_opened = ~Q(date_opened__gt=timezone.now() - timezone.timedelta(days=40))

    # workshoprepairs = WorkshopRepair.objects.filter(hi_or_ho | not_recently_opened
    # )
    
    # we want to find all sales where:
    #   - profit is greater than expenditure 
    #   - workshop name contains a number

    name_has_num = Q(workshoprepair__name__regex=r"[A]+")
    profited = Q(income__gt=F('expenditure'))

    sales1 = Sale.objects.filter(name_has_num & profited)
    sales2 = Sale.objects.filter(name_has_num | profited)
    sales = Sale.objects.select_related('workshoprepair').filter(name_has_num | profited)

    print(sales)

    # for sale in sales:
    #     if sale.income <= sale.expenditure:
    #         print(sale.workshoprepair.name)

    pprint(connection.queries)