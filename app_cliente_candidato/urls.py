from django.urls import path
from .views import (
    ClienteCandidatoCreateView,
    ClienteCandidatoListView,
    ClienteCandidatoDetailView,
    ClienteCandidatoUpdateView,
    ClienteCandidatoDeleteView,
    ExportarCandidatosExcel,
)

urlpatterns = [
    path('candidatos/crear/', ClienteCandidatoCreateView.as_view(), name='crear'),
    path('candidatos/listar/', ClienteCandidatoListView.as_view(), name='listar'),
    path('candidatos/detalle/<int:pk>/', ClienteCandidatoDetailView.as_view(), name='detalle'),
    path('candidatos/actualizar/<int:pk>/', ClienteCandidatoUpdateView.as_view(), name='actualizar'),
    path('candidatos/eliminar/<int:pk>/', ClienteCandidatoDeleteView.as_view(), name='eliminar'),
    path('candidatos/exportar/', ExportarCandidatosExcel.as_view(), name='exportar_excel'),
]