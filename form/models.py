from django.db import models

# Create your models here.\
class Kota(models.Model):
    id = models.AutoField(primary_key=True)
    kota = models.CharField(max_length=50)

    class Meta:
        db_table = 'kota'
        managed = True
        verbose_name = 'kota'

class Form(models.Model):
    id = models.AutoField(primary_key=True)
    pinjaman = models.IntegerField()
    tenor = models.CharField(max_length=1)
    angsuran = models.IntegerField()
    nama = models.CharField(max_length=60)
    telp = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)
    alamat = models.TextField()
    kota_id = models.ForeignKey(Kota, db_column='kota_id', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'form'
        managed = True
        verbose_name = 'form'