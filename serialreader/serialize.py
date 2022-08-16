from pyexpat import model
from rest_framework import serializers
from serialreader.models import DetailsModel

class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailsModel
        fields = "__all__"