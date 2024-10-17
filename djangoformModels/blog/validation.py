from django.core.exceptions import ValidationError


user_not_post = ['admin', 'operator', 'teknisi']
def validate_writer(value):
    if value in user_not_post:
        raise ValidationError(f'{value} Tidak Bisa Mengirim')

def validate_article(value):
    if len(value) < 100:
        raise ValidationError('Masukan Artikel Lebih Dari 100 Karakter')
