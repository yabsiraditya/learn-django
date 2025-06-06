from django import forms

class FormsFields(forms.Form):
    # numeric data type
    integer_field = forms.IntegerField(required=False)
    decimal_field = forms.DecimalField(required=False)
    float_field = forms.FloatField(required=False)

    # string data type
    char_field = forms.CharField(required=False)
    email_field = forms.EmailField()
    slug_field = forms.SlugField()
    regex_field = forms.RegexField(regex=r'(P?<input>)')
    url_field = forms.URLField()
    ipaddress_field = forms.GenericIPAddressField()


    # select input type 
    PILIHAN = (
        ('Pilihan1','Pilihan1'),
        ('Pilihan2','Pilihan2'),
        ('Pilihan3','Pilihan3'),
    )

    choice_field = forms.ChoiceField(choices=PILIHAN)
    multy_choice_field = forms.MultipleChoiceField(choices=PILIHAN)
    type_choice_field = forms.TypedChoiceField(choices=PILIHAN)
    multy_typed_field = forms.TypedMultipleChoiceField(choices=PILIHAN)
    null_boolean_field = forms.NullBooleanField() 

    # date time type
    date_field = forms.DateField()
    datetime_field = forms.DateTimeField()
    durasi_field = forms.DurationField()
    time_field = forms.TimeField()
    splitdatetime_field = forms.SplitDateTimeField()

    # fiel input type
    file_field = forms.FileField()
    image_field = forms.ImageField()

    # other field
    boolean_field = forms.BooleanField()
    uuid_field = forms.UUIDField()
    json_field = forms.JSONField()
    file_path_field = forms.FilePathField(path='mysite/', allow_files=True, allow_folders=True)