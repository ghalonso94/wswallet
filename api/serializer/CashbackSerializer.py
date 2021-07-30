from rest_framework import serializers, status
from rest_framework.response import Response

from core.models import Cashback


class CashbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cashback
        fields = '__all__'

