from core.models import WorkshopRepair, User, Rating, Sale, Staff, StaffWorkshoprepair
from django.utils import timezone
from django.db import connection
from pprint import pprint
from django.db.models.functions import Lower
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


    staff, created = Staff.objects.get_or_create(
        name='John Dhoe'
    )

    staff.workshoprepairs.set(
        WorkshopRepair.objects.all()[:5],
        through_defaults={'salary':random.randint(20_000, 80_000)}
    )

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