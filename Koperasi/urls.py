from django.urls import path
from . import views

urlpatterns = [
    path("kasir/", views.KasirListCreate.as_view(), name="Kasir-views-create"),
    path("kasir/<int:pk>/", views.KasirRetrieveUpdateDestroy.as_view(), name="Update"),
]