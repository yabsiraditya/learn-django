from django.test import TestCase
from core.models import WorkshopRepair

# Create your tests here.
class WorkshoprepiarTest(TestCase):
    def test_workshoprepair_name_property(self):
        workshoprepair = WorkshopRepair(name="test")
        self.assertEqual(workshoprepair.workshoprepair__name, 'test')


        workshoprepair.nickname = "asdasdasd"
        self.assertEqual(workshoprepair.workshoprepair__name, 'asdasdasd')