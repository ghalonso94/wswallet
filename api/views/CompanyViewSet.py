from rest_framework import viewsets
from core.models import Company
from api.serializer import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):

    # Show all companies
    queryset = Company.objects.all()
    serializer_class = CompanySerializer