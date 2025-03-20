from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("paytono_failai.urls", namespace="paytono_failai")),
]
