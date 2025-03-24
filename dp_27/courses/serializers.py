from rest_framework import serializers
from .models import UserCertificate

class UserCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCertificate
        fields = '__all__'
