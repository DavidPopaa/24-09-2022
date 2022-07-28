from django.contrib import admin
from django.urls import path, include
from crud import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.DetailsTable.as_view()),
    path("accounts/", include("accounts.urls")),
    path("auth/", obtain_auth_token)
]
