from django.db import models

# Create your models here.
class Produk(models.Model):
    jenis_barang = models.CharField(max_length=100)  
    nama_barang = models.TextField()


    def __str__(self):
        return self.jenis_barang

class Kasir(models.Model):
    Produk = models.ForeignKey(Produk, related_name="kasir", on_delete=models.CASCADE)
    id_barang = models.CharField(max_length=100)
    total_pembayaran = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.id_barang

class Pembeli(models.Model):
    nama_barang = models.CharField(max_length=100)
    pembayaran = models.TextField() 

    def __str__(self):
        return self.pembayaran       

