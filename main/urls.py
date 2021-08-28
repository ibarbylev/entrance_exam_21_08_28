from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('rest-api/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
