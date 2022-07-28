
from . import serialize
from crud.models import DetailsModel
from crud.serialize import DetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serialReader import dist

class DetailsTable(APIView):
    def get(self,request):
        DetailsModel.objects.all().delete()
        new_data = DetailsModel(dist1=dist[0], dist2=dist[1], dist3=dist[2], dist4=dist[3])
        new_data.save()
        detailsObj = DetailsModel.objects.all()
        dlSerializeObj = DetailsSerializer(detailsObj,many=True)
        return Response(dlSerializeObj.data)