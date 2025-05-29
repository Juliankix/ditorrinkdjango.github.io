from django.urls import path
from .views import (
    ClienteCandidatoCreateView,
    ClienteCandidatoListView,
    ClienteCandidatoDetailView,
    ClienteCandidatoUpdateView,
    ClienteCandidatoDeleteView,
)

urlpatterns = [
    path('crear/', ClienteCandidatoCreateView.as_view(), name='cliente-candidato-crear'),  # POST
    path('listar/', ClienteCandidatoListView.as_view(), name='cliente-candidato-listar'),  # GET
    path('detalle/<int:pk>/', ClienteCandidatoDetailView.as_view(), name='cliente-candidato-detalle'),  # GET
    path('actualizar/<int:pk>/', ClienteCandidatoUpdateView.as_view(), name='cliente-candidato-actualizar'),  # PUT/PATCH
    path('eliminar/<int:pk>/', ClienteCandidatoDeleteView.as_view(), name='cliente-candidato-eliminar'),  # DELETE
]
