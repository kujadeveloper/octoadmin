from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework import status

shema = {
	'SearchView':{
		'search':openapi.Schema(
					type=openapi.TYPE_OBJECT,
					properties={
						'query': openapi.Schema(
							type=openapi.TYPE_STRING
						)
					}
		),
	},

}