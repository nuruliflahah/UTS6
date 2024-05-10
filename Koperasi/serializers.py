from rest_framework import serializers
from .models import Produk, Kasir, Pembeli

class ProdukSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = ["id", "jenis_barang", "nama_barang"]

class KasirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kasir
        fields = ["id","produk", "id_barang", "total_pembyaran", "published_date"]

class PembeliSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembeli
        fields = ["id", "nama_barang", "pembayaran"]                 