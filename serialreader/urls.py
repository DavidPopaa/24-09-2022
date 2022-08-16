from django.urls import path
from serialreader import views

urlpatterns = [
    path("", views.DetailsTable.as_view()),
]
