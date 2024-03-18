from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import render

from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import status, viewsets
from rest_framework.response import Response

from elasticsearch_dsl import Q, A

from .documents import OctoDocument
from .shema import shema
from .serializers import OctoSerializer

class SearchView(viewsets.ModelViewSet):
	permission_classes = [IsAuthenticated]

	@swagger_auto_schema(request_body=shema['SearchView']['search'])
	def list(self, request):
		query = request.data.get('query')
		if not query:
			return Response({'error': 'Query not provided'}, status=400)
	
		filter_query = Q("wildcard", Hostname=f"*{query}*")
		search = OctoDocument.search().query(filter_query)
		response = search.execute()
		serializer = OctoSerializer(response, many=True)
		return Response({'query': serializer.data})