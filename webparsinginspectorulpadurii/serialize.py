from pyexpat import model
from rest_framework import serializers
from webparsinginspectorulpadurii.models import MetriCubiModel, NotOkMetriCubi, IstoricMetriCubi

class MetriCubiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetriCubiModel
        fields = "__all__"
    
class NotOkMetriCubiSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotOkMetriCubi
        fields = "__all__"
        
class IstoricMetriCubiSerializer(serializers.ModelSerializer):
    class Meta:
        model = IstoricMetriCubi
        fields = "__all__"

