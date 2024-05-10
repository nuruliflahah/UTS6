from django.urls import path
from . import views

urlpatterns = [
    path("kasir/", views.KasirListCreate.as_view(), name="Kasir-views-create"),
    path("kasir/<int:pk>/", views.KasirRetrieveUpdateDestroy.as_view(), name="Update"),
    path("produk/", views.ProdukListCreate.as_view(), name="Produk-views-create"),
    path("produk/<int:pk>/", views.PembeliRetrieveUpdateDestroy.as_view(), name="Update"),
    path("pembeli/", views.ProdukListCreate.as_view(), name="Produk-views-create"),
    path("pembeli/<int:pk>/", views.PembeliRetrieveUpdateDestroy.as_view(), name="Update"),
    
]
