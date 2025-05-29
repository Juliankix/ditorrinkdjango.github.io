from rest_framework import generics, permissions
from .models import Administrador
from .serializers import AdminSerializer

# Crear administrador (POST)
class AdministradorCreateView(generics.CreateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]

# Listar administradores (GET)
class AdministradorListView(generics.ListAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]

# Ver detalle de un administrador específico (GET)
class AdministradorDetailView(generics.RetrieveAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

# Actualizar administrador (PUT/PATCH)
class AdministradorUpdateView(generics.UpdateAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]

# Eliminar administrador (DELETE)
class AdministradorDeleteView(generics.DestroyAPIView):
    queryset = Administrador.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.IsAuthenticated]
