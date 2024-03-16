# backend/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("api.urls")),  # Include the root URL pattern for the API
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

# Add static and media URLs if needed
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

