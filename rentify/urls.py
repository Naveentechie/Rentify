from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),  # Include the URLs from your app
    path('admin/', admin.site.urls),
]
