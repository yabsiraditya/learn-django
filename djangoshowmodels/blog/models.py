from django.db import models

# Create your models here.
class Kategori(models.Model):
    kode = models.CharField(max_length=7)
    nama = models.CharField(max_length=255)

    def __str__(self):
        return "%d. %s" % (self.id, self.nama)
    

class Artikel(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    pilih_kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)

    def __str__(self):
        return "%d. %s" % (self.id, self.judul)
    