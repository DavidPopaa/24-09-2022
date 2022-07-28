from django.urls import path, include
from rest_framework import routers
from .views import UserModel, BookView

router = routers.DefaultRouter()
router.register("users", UserModel)
router.register("books", BookView)

urlpatterns = [ 
    path("", include(router.urls)),
]
