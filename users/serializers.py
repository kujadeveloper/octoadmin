from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            try:
                validate_password(password)
            except ValidationError as e:
                print(e)  # Handle the error by informing the user of password requirements
                raise serializers.ValidationError(e)
            instance.set_password(password)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            try:
                validate_password(password)
            except ValidationError as e:
                print(e)  # Handle the error by informing the user of password requirements
                raise serializers.ValidationError(e)
            
            instance.set_password(password)

        instance.save()
        return instance