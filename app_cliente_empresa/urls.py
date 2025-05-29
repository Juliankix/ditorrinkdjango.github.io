from django.urls import path
from .views import (
    ClienteEmpresaCreateView,
    ClienteEmpresaListView,
    ClienteEmpresaDetailView,
    ClienteEmpresaUpdateView,
    ClienteEmpresaDeleteView
)

urlpatterns = [
    path('crear/', ClienteEmpresaCreateView.as_view(), name='cliente-empresa-crear'),       # POST
    path('listar/', ClienteEmpresaListView.as_view(), name='cliente-empresa-listar'),       # GET
    path('detalle/<int:pk>/', ClienteEmpresaDetailView.as_view(), name='cliente-empresa-detalle'),  # GET
    path('actualizar/<int:pk>/', ClienteEmpresaUpdateView.as_view(), name='cliente-empresa-actualizar'),  # PUT/PATCH
    path('eliminar/<int:pk>/', ClienteEmpresaDeleteView.as_view(), name='cliente-empresa-eliminar'),  # DELETE
]
