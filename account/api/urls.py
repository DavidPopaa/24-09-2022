from django.urls import path, include
from . import views
from .views import MyTokenObtainPairView, UserModel
from rest_framework import routers



from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register("register", UserModel)



urlpatterns = [
    # path('', views.getRoutes),
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
