from django.contrib import admin
from django.urls import include, path
import voiceClonerApp

urlpatterns = [
    path("voiceClone/", include("voiceClonerApp.urls")),
    path("admin/", admin.site.urls),
]