from core.models import WorkshopRepair, User, Rating
from django.utils import timezone
from django.db import connection

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

    print(Rating.objects.exclude(rating__lte=3))
    print(connection.queries)