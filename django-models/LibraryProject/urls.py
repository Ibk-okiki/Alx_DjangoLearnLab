# LibraryProject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Include all URLs from relationship_app
    path('', include('relationship_app.urls')),
]
