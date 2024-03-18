import json
import os
import base64

from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.exceptions import ValidationError

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import UserSerializer
from .models import User
from .shema import shema

from utils.utils import *

class UsersPublicView(viewsets.ModelViewSet):
	permission_classes = [AllowAny]
	serializer_class = UserSerializer

	@swagger_auto_schema(request_body=shema['UsersView']['create'],
		operation_description=shema['UsersView']['create_descriptions'])
	def create(self, request):
		request.data['username'] = request.data['username']
		if request.data['password']!=request.data['repassword']:
			raise ValidationError('Password not match')

		request.data['confirm_code'] = generate_random_string()
		serializer = UserSerializer(data = request.data)
		serializer.is_valid(raise_exception=True)
		serializer.save()
		return Response({'success':True,'message':'Kayıt oluşturuldu.', 'data':serializer.data})

	
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
	
	def get_token(self, user):
		if user.is_deleted:
			raise ValidationError({'detail':'Not found'})
		token = super().get_token(user)
		token['username'] = user.username
		return token

	def validate(self, attrs):
		data = super().validate(attrs)
			
		encoded_username = base64.b64encode(data['access'].encode()).decode()
		data['access'] = encoded_username
		return data