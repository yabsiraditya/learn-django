from django import forms

import datetime as datetime

JENIS_KELAMIN = (
    ('p','Pria'),
    ('w','Wanita'),
)

TAHUN = range(1, datetime.date.today().year+1, 1)
today = datetime.date.today()
MONTHYEAR = datetime.date(today.year, today.month, 1)

class KontakForms(forms.Form):
    nama = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Alamat Email', help_text='Masukan Alamat Email Dengan Benar')
    no_telp = forms.IntegerField(required=False)
    tgl_lahir = forms.DateField(
        initial=MONTHYEAR,
        widget = forms.SelectDateWidget(
            years=TAHUN,
        ),
    )
    jenkel = forms.ChoiceField(
        choices = JENIS_KELAMIN, 
        label = 'Jenis Kelamin',
        widget = forms.RadioSelect(), 
    )
    subjek = forms.CharField(required=False)
    pesan = forms.CharField(required=False)
    alamat = forms.CharField(
        widget = forms.Textarea(),
    )

    aggre = forms.BooleanField()