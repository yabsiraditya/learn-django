from django import forms

# import models
from.models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nameCustomer'].widget.attrs.update(
            {
                'class':'form-control'
            }
        )

        self.fields['nameDriver'].widget.attrs.update(
            {
                'class':'form-control'
            }
        )

        self.fields['destination'].widget.attrs.update(
            {
                'class':'form-control'
            }
        )