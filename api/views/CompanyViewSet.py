from rest_framework import viewsets
from core.models import Company
from api.serializer import CompanySerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CompanyViewSet(viewsets.ModelViewSet):

    # Show all companies
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]