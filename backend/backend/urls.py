from django.contrib import admin
from django.urls import include, path
from website_deploy.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sql_generator.urls')),
    path('health/', health_check, name='health_check'),
]
