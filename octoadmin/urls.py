from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path, include, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from users.views import CustomTokenObtainPairSerializer

schema_view = get_schema_view(
   openapi.Info(
      title="Octoadmin",
      default_version='v1',
      description="Octoadmin Page",
      terms_of_service="https://www.octoadmin.com/terms/",
      contact=openapi.Contact(email="info@octoadmin.com"),
      license=openapi.License(name="octoadmin")
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


versions = 'v1/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('token/', TokenObtainPairView.as_view(serializer_class=CustomTokenObtainPairSerializer), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', include('users.urls')),
    path('search/', include('search.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)