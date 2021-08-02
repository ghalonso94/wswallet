from rest_framework import serializers

from core.models import Cashback


class CashbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cashback
        fields = '__all__'

