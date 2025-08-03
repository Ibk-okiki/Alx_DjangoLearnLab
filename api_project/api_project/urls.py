from django.contrib import admin
from django.urls import path, include  # Include added here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # API routing added
]
