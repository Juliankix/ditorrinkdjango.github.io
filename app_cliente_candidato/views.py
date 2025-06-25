from rest_framework import generics
from rest_framework.views import APIView
from django.http import HttpResponse
from .models import ClienteCandidato
from .serializers import ClienteCandidatoSerializer
import pandas as pd
import io

# Tus vistas generics
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

class ExportarCandidatosExcel(APIView):
    #permission_classes = [IsAdminUser]  # opcional

    def get(self, request, format=None):
        candidatos = ClienteCandidato.objects.all().values()
        df = pd.DataFrame(list(candidatos))

        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Candidatos')

        output.seek(0)
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="candidatos.xlsx"'
        return response
