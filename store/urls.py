from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("products.urls")),
    path("api/", include("accounts.urls")),
    path('accounts/', include('allauth.urls')),
    path("api/auth/", include("rest_auth.urls")),
    path("api/auth/registration/", include("rest_auth.registration.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
