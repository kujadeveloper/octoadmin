from django.urls import path
from .views import SearchView

urlpatterns = [
    path('', SearchView.as_view({'post':'list'}), name='search_view')
]