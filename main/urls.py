from django.urls import path
from .views import EnglishViewSet

urlpatterns = [
    path('', EnglishViewSet.as_view({'get': 'list'}), name='english'),
]