from django.db import models

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} {self.nama}"
    

class Artikel(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    pilih_kategori = models.ForeignKey(
        Kategori, on_delete=models.CASCADE, default=0
    )
    tanggal_publik = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id} {self.judul}"
