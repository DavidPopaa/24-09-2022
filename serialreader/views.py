from . import serialize
from .models import DetailsModel
from .serialize import DetailsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import serial.tools.list_ports

class DetailsTable(APIView):
    def post(self,request):
        ports= serial.tools.list_ports.comports()
        serialInst=serial.Serial()
        portsList=[]

        for onePort in ports:
            portsList.append(str(onePort))
            print(str(onePort))

        # val=input("select port: COM")
        val_request = request.data
        val = val_request['com_number']
        

        for x in range(0, len(portsList)):
            if portsList[x].startswith("COM"+str(val)):
                portVar="COM"+str(val)
                print(portsList[x])
        serialInst.baudrate=9600
        serialInst.port=portVar
        serialInst.open()
        i = 0
        dist = []
        while i <= 3:
            if serialInst.in_waiting:
                packet=serialInst.readline()
                print(packet.decode("utf-8"))
                data = packet.decode("utf-8")
                for s in data.split():
                    try:
                        dist.append(float(s))
                    except ValueError:
                        pass 
                i = i + 1


        DetailsModel.objects.all().delete()
        new_data = DetailsModel(dist1=dist[0], dist2=dist[1], dist3=dist[2], dist4=dist[3])
        new_data.save()
        detailsObj = DetailsModel.objects.all()
        dlSerializeObj = DetailsSerializer(detailsObj,many=True)
        return Response(dlSerializeObj.data)