from rest_framework.response import Response
from rest_framework.views import APIView
from webparsinginspectorulpadurii.models import MetriCubiModel, NotOkMetriCubi, IstoricMetriCubi
from webparsinginspectorulpadurii.serialize import MetriCubiSerializer
import json
import time
import requests
from .serialize import IstoricMetriCubiSerializer, NotOkMetriCubiSerializer



class DisplayIstoricMetriCubi(APIView):
    def get(self, request):
        list_with_metricubi = IstoricMetriCubi.objects.all()
        SerilizedObject = IstoricMetriCubiSerializer(list_with_metricubi,many=True)
        return Response(SerilizedObject.data)

class DisplayNuOkMetriCubi(APIView):
    def get(self, request):
        list_with_nu_ok_metri_cubi = NotOkMetriCubi.objects.all()
        SerilizedObjectt = NotOkMetriCubiSerializer(list_with_nu_ok_metri_cubi,many=True)
        return Response(SerilizedObjectt.data)
        

class DisplayMetriCubi(APIView):
    # def get(self, request):
    #     MetriCubiModel.objects.all().delete()
    #     new_data = MetriCubiModel(array_de_metri_cubi=array_de_exportat_metri_cubi)
    #     new_data.save()
    #     all_new_objects = MetriCubiModel.objects.all()
    #     SerializeObject = MetriCubiSerializer(all_new_objects,many=True)
    #     return Response(SerializeObject.data)
    
    def post(self, request):
        # post_data = request.data
        # nr_auto = post_data['nr_placuta']
        # print(nr_auto)
        # print(type(nr_auto))
        # print("loading...")
        nr_auto = "CJ69SCM"
        response = requests.get(f"https://inspectorulpadurii.ro/api/aviz/locations?nr={nr_auto}&cod=&nrApv=&tip=")


        data = json.loads(response.text)
        # ca sa convertesc din string in ditcionary
        print(data)
        print(type(data))


        array_de_data = []
        for item in data:
            array_de_data.append(data[item])
    # iau datele din dictionar si le mut in array, facand un array de array-uri


        # codul_avizului = array_de_data[1][0]

        array_de_exportat_metri_cubi = []
        for item in array_de_data[1]:
            time.sleep(1)
            responseee = requests.get(f"https://inspectorulpadurii.ro/api/aviz/{item}")
            decoded_responsee = responseee.json()
            del decoded_responsee['poze']
            print("=================")
            print(decoded_responsee['marfa']['total'])
            array_de_exportat_metri_cubi.append(decoded_responsee['marfa']['total'])


        print("array de exportat:")
        print(array_de_exportat_metri_cubi)
        x = 1.86
        y = array_de_exportat_metri_cubi[0]
        istoric_metri_cubi_variable = IstoricMetriCubi(nr_inmatriculare=nr_auto,volum_detectat=x,volum_avizat=y)
        istoric_metri_cubi_variable.save()
        if(not(x >= (9*y)/10 and x <= (11*y)/10)):
            not_ok_metri_cubi = NotOkMetriCubi(nr_inmatriculare=nr_auto,volum_detectat=x,volum_avizat=y)
            not_ok_metri_cubi.save()
            
        
        MetriCubiModel.objects.all().delete()
        new_data = MetriCubiModel(array_de_metri_cubi=array_de_exportat_metri_cubi)
        new_data.save()
        all_new_objects = MetriCubiModel.objects.all()
        SerializeObject = MetriCubiSerializer(all_new_objects,many=True)
        return Response(SerializeObject.data)
        

