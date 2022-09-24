from rest_framework import serializers
from serialreader.models import DetailsModel, PressComModel

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsModel
        fields = "__all__"


class PressComModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PressComModel
        fields = "__all__"
        
    