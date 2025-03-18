from core.models import WorkshopRepair, User, Rating, Sale
from django.utils import timezone
from django.db import connection
from pprint import pprint

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


    WorkshopRepair.objects.all().delete()


    pprint(connection.queries)