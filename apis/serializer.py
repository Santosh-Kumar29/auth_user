from rest_framework import serializers
from .models import UserMaster


class UserMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMaster
        fields = '__all__'
