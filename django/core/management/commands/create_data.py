import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import WorkshopRepair, Rating, Sale


class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        # get or create an admin user
        user = User.objects.filter(username='admin')
        if not user.exists():
            user = User.objects.create_superuser(username='admin', password='test')
        else:
            user = user.first()

        workshoprepairs = [
            {'name': 'Astra Honda Motor Cibinong', 'date_opened': timezone.now() - timezone.timedelta(days=20), 'workshop_type': WorkshopRepair.TypeWorkshop.MOTORCYCLE, 'latitude': -6.471241834712562, 'longitude': 106.86184842624745},
            {'name': 'Yamaha Service Center Mekar Motor', 'date_opened': timezone.now() - timezone.timedelta(days=27), 'workshop_type': WorkshopRepair.TypeWorkshop.MOTORCYCLE, 'latitude': -6.470738718819811, 'longitude': 106.86106443120711}, 
            {'name': 'Plaza Toyota Citeureup', 'date_opened': timezone.now() - timezone.timedelta(days=15), 'workshop_type': WorkshopRepair.TypeWorkshop.CAR, 'latitude': -6.4838457217652765, 'longitude': 106.87035073816715}, 
            {'name': 'Honda Internusa Cibinong', 'date_opened': timezone.now() - timezone.timedelta(days=44), 'workshop_type': WorkshopRepair.TypeWorkshop.CAR, 'latitude': -6.481702698731912, 'longitude': 106.86930378329876},
            {'name': 'Shell Helix Autocare Wijaya Motor', 'date_opened': timezone.now() - timezone.timedelta(days=51), 'workshop_type': WorkshopRepair.TypeWorkshop.CAR, 'latitude': -6.47749247014144, 'longitude': 106.8831463804008},
            {'name': 'Hino Hudaya Bogor', 'date_opened': timezone.now() - timezone.timedelta(days=12), 'workshop_type': WorkshopRepair.TypeWorkshop.BUSTRUCK, 'latitude': -6.519983738218839, 'longitude': 106.83833715078336},
            {'name': 'Astra Daihatsu Cibinong', 'date_opened': timezone.now() - timezone.timedelta(days=31), 'workshop_type': WorkshopRepair.TypeWorkshop.CAR, 'latitude': -6.473310292796284, 'longitude': 106.84785290586139},
            {'name': 'Hyundai Cibinong Official', 'date_opened': timezone.now() - timezone.timedelta(days=71), 'workshop_type': WorkshopRepair.TypeWorkshop.CAR, 'latitude': -6.5057493144999565, 'longitude':  106.84247897833534},
            {'name': 'DEALER VESPA MATIC PIAGGIO BOGOR PAJAJARAN. (MARKETING AGLY)', 'date_opened': timezone.now() - timezone.timedelta(days=46), 'workshop_type': WorkshopRepair.TypeWorkshop.MOTORCYCLE, 'latitude': -6.601126190892277, 'longitude': 106.80705036940182},
        ]

        WorkshopRepair.objects.all().delete()
        for r in workshoprepairs:
            WorkshopRepair.objects.create(**r)

        workshoprepairs = WorkshopRepair.objects.all()

        # create some ratings
        for _ in range(30):
            Rating.objects.create(
                workshoprepair=random.choice(workshoprepairs),
                user=user,
                rating=random.randint(1,5)
            )

        # create some sales
        for _ in range(100):
            Sale.objects.create(
                workshoprepair=random.choice(workshoprepairs),
                income=random.uniform(5, 100),
                datetime=timezone.now() - timezone.timedelta(days=random.randint(1,50))
            )