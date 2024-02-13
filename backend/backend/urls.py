from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sql_generator.urls')),
    path('health/', health_check, name='health_check'),
]
