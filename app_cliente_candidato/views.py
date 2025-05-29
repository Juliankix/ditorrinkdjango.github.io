from rest_framework import generics
from .models import ClienteCandidato
from .serializers import ClienteCandidatoSerializer

class ClienteCandidatoCreateView(generics.CreateAPIView):
    queryset = ClienteCandidato.objects.all()
    serializer_class = ClienteCandidatoSerializer

class ClienteCandidatoListView(generics.ListAPIView):
    queryset = ClienteCandidato.objects.all()
    serializer_class = ClienteCandidatoSerializer

class ClienteCandidatoDetailView(generics.RetrieveAPIView):
    queryset = ClienteCandidato.objects.all()
    serializer_class = ClienteCandidatoSerializer

class ClienteCandidatoUpdateView(generics.UpdateAPIView):
    queryset = ClienteCandidato.objects.all()
    serializer_class = ClienteCandidatoSerializer

class ClienteCandidatoDeleteView(generics.DestroyAPIView):
    queryset = ClienteCandidato.objects.all()
    serializer_class = ClienteCandidatoSerializer
