from rest_framework import viewsets
from core.models import Client
from api.serializer import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):

    # Show all clients
    queryset = Client.objects.all()
    serializer_class = ClientSerializer