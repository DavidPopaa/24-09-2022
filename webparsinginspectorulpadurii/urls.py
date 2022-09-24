from django.urls import path
from webparsinginspectorulpadurii import views


urlpatterns = [
    path("", views.DisplayMetriCubi.as_view()),
    path("listmetricubi/", views.DisplayIstoricMetriCubi.as_view()),
    path("notokmetricubi/",views.DisplayNuOkMetriCubi.as_view())
]
