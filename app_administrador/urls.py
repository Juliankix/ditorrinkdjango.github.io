from django.urls import path
from .views import AdministradorCreateView, AdministradorListView, AdministradorDetailView, AdministradorUpdateView, AdministradorDeleteView

urlpatterns = [
    path('crear/', AdministradorCreateView.as_view(), name='candidato-crear'),  # POST
    path('listar/', AdministradorListView.as_view(), name='candidato-listar'),  # GET
    path('detalle/<int:pk>/', AdministradorDetailView.as_view(), name='candidato-detalle'),  # GET
    path('actualizar/<int:pk>/', AdministradorUpdateView.as_view(), name='candidato-actualizar'),  # PUT/PATCH
    path('eliminar/<int:pk>/', AdministradorDeleteView.as_view(), name='candidato-eliminar'),  # DELETE
]