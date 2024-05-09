from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Kasir
from .serializers import KasirSerializer
from rest_framework.views import APIView

class KasirListCreate(generics.ListCreateAPIView):
    queryset = Kasir.objects.all()
    serializer_class = KasirSerializer

class KasirRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kasir.objects.all()
    serializer_class = KasirSerializer
    lookup_field = "pk"