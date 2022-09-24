from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", obtain_auth_token),
    path("api/", include("account.api.urls")),
    path("serial/", include("serialreader.urls")),
    path("metricubi/", include("webparsinginspectorulpadurii.urls"))
]