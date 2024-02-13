from django.urls import path
from .views import generate_sql

urlpatterns = [
    path('generate', generate_sql),
]
