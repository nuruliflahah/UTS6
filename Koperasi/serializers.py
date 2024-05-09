from rest_framework import serializers
from .models import Kasir

class KasirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kasir
        fields = ["id", "nama_barang", "harga", "published_date"]