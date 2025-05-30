from rest_framework import generics
from app_cliente_empresa.models import ClienteEmpresa
from app_cliente_empresa.serializers import ClienteEmpresaSerializer

class ClienteEmpresaCreateView(generics.CreateAPIView):
    queryset = ClienteEmpresa.objects.all()
    serializer_class = ClienteEmpresaSerializer

class ClienteEmpresaListView(generics.ListAPIView):
    queryset = ClienteEmpresa.objects.all()
    serializer_class = ClienteEmpresaSerializer

class ClienteEmpresaDetailView(generics.RetrieveAPIView):
    queryset = ClienteEmpresa.objects.all()
    serializer_class = ClienteEmpresaSerializer

class ClienteEmpresaUpdateView(generics.UpdateAPIView):
    queryset = ClienteEmpresa.objects.all()
    serializer_class = ClienteEmpresaSerializer

class ClienteEmpresaDeleteView(generics.DestroyAPIView):
    queryset = ClienteEmpresa.objects.all()
    serializer_class = ClienteEmpresaSerializer
