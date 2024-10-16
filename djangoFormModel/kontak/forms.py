from django import forms

class KontakForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    message = forms.CharField(
        widget= forms.Textarea()
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'yabsir.aditya@gmail.com' in email:
            raise forms.ValidationError(f'Email {email} ini sudah mengirim pesan')

    def __str__(self):
        return "%d %s" & (self.id, self.name)