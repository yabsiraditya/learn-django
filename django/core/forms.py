from django import forms
from core.models import Rating, WorkshopRepair, Order


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('workshoprepair', 'user', 'rating')


class WorkshopForm(forms.ModelForm):
    class Meta:
        model = WorkshopRepair
        fields = ('name', 'workshop_type')


class ProductStockException(Exception):
    pass


class ProductOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'number_of_items')


    def save(self, commit = True):
        """ Check to see if the product has enough items in stock """
        order = super().save(commit=False)
        if order.product.number_in_stock < order.number_of_items:
            raise ProductStockException(
                f"Not enough items in stock for product: {order.product}"
            )
        if commit:
            order.save()
        return order