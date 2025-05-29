from rest_framework import generics
from .models import ClienteEmpresa
from .serializers import ClienteEmpresaSerializer, ClienteEmpresaRegistroSerializer

# Crear cliente empresa (POST)
class ClienteEmpresaCreateView(generics.CreateAPIView):
    queryset = ClienteEmpresa.objects.all()
    serializer_class = ClienteEmpresaRegistroSerializer

# Listar clientes empresa (GET)
class ClienteEmpresaListView(generics.ListAPIView):
    queryset = ClienteEmpresa.objects.all()
    serializer_class = ClienteEmpresaSerializer

# Ver detalle de cliente empresa (GET)
class ClienteEmpresaDetailView(generics.RetrieveAPIView):
    queryset = ClienteEmpresa.objects.all()
    serializer_class = ClienteEmpresaSerializer

# Actualizar cliente empresa (PUT/PATCH)
class ClienteEmpresaUpdateView(generics.UpdateAPIView):
    queryset = ClienteEmpresa.objects.all()
    serializer_class = ClienteEmpresaRegistroSerializer

# Eliminar cliente empresa (DELETE)
class ClienteEmpresaDeleteView(generics.DestroyAPIView):
    queryset = ClienteEmpresa.objects.all()
    serializer_class = ClienteEmpresaSerializer
