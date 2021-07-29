from rest_framework import viewsets
from core.models import Cashback
from api.serializer import CashbackSerializer


class CashbackViewSet(viewsets.ModelViewSet):

    # Show all clients
    queryset = Cashback.objects.all()
    serializer_class = CashbackSerializer