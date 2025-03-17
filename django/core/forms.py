from django import forms
from core.models import Rating, WorkshopRepair


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('workshoprepair', 'user', 'rating')


class WorkshopForm(forms.ModelForm):
    class Meta:
        model = WorkshopRepair
        fields = ('name', 'workshop_type')