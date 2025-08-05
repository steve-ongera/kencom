from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler403, handler404, handler500
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("website.urls")),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Error handlers
handler400 = 'website.views.custom_bad_request'
handler403 = 'website.views.custom_permission_denied'
handler404 = 'website.views.handler404'
handler500 = 'website.views.handler500'
