from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Kasir, Produk, Pembeli
from .serializers import KasirSerializer, ProdukSerializer, PembeliSerializer
from rest_framework.views import APIView

class KasirListCreate(generics.ListCreateAPIView):
    queryset = Kasir.objects.all()
    serializer_class = KasirSerializer

class KasirRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kasir.objects.all()
    serializer_class = KasirSerializer
    lookup_field = "pk" 

class ProdukListCreate(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer

class ProdukRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProdukSerializer
    lookup_field = "pk"  

class PembeliListCreate(generics.ListCreateAPIView):
    queryset = Pembeli.objects.all()
    serializer_class = PembeliSerializer

class PembeliRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pembeli.objects.all()
    serializer_class = PembeliSerializer
    lookup_field = "pk"        