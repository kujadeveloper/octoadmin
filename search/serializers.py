from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework import serializers
from search.models import OctoModel


class OctoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoModel
        fields = ['Hostname']
