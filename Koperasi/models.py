from django.db import models

# Create your models here.
class Kasir(models.Model):
    nama_barang = models.CharField(max_length=100)
    harga = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_barang


class Produk(models.Model):
    kasir = models.ForeignKey(Kasir, related_name="produk", on_delete=models.CASCADE)
    jenis_barang = models.CharField(max_length=100)  
    nama_barang = models.TextField()

    def __str__(self):
        return self.jenis_barang

class Pembeli(models.Model):
    nama_barang = models.CharField(max_length=100)
    pembayaran = models.TextField() 

    def __str__(self):
        return self.pembayaran       

