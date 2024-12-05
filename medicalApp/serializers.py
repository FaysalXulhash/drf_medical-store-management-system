from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'license_num', 'address', 'contact', 'email', 'description', 'added_on']
