
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trade-api/', include('app.urls')),  # Include core app's URLs'
    # path('trade-api/', include('test_app.urls')),  # Include core app's URLs'
]
