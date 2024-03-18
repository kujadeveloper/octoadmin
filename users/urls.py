from django.urls import path
from .views import UsersPublicView

urlpatterns = [
    path('registry', UsersPublicView.as_view({'post':'create'}), name='users')
]