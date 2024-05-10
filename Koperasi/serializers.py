from rest_framework import serializers
from .models import Kasir, Produk, Pembeli

class KasirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kasir
        fields = ["id", "nama_barang", "harga", "published_date"]

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ["id", "jenis_barang", "nama_barang"]

class PembeliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembeli
        fields = ["id", "nama_barang", "pembayaran"]                 