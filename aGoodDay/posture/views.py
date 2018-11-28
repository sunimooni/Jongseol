from rest_framework import status
from posture.models import Device, Posture
from posture.serializers import DeviceSerializer, PostureSerializer
from rest_framework import  generics, status, viewsets
from rest_framework.response import Response
from datetime import date, timedelta



"""
@file   aGoodDay.posture.views
@brief  Recevied device_id and start_date, end_date from GET request, and return user posture data
@author jeje(las9897@gmail.com)
@param  int device_id | string start_date | string end_date
@return array
"""
class DeviceDetail(generics.ListCreateAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        device_id = self.kwargs['device_id']
        #today = self.request.GET.get('today')
        today = date.today() + timedelta(days=1)
        pre_day = today - timedelta(days=7)
        return Device.objects.filter(device_id=device_id, date__range=[pre_day, today])
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

"""
@brief  after receiving dataform from POST request, insert posture to MySQL.
        Both single data and multi data are possible.
@author jeje(las9897@gmail.com)
@param  jsonarray dataform
@return int responsecode
"""
'''
class DeviceInsert(generics.CreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data,list))
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
'''

class PostureDetail(generics.ListCreateAPIView):
    serializer_class = PostureSerializer
    def get_queryset(self):
        device_id = self.kwargs['device_id']
        return Posture.objects.filter(device_id=device_id)

class PostureUpdate(generics.UpdateAPIView):
    queryset = Posture.objects.all()
    serializer_class = PostureSerializer
    lookup_field = 'device_id'

    def get_queryset(self):
        device_id = self.kwargs['device_id']
        return Posture.objects.filter(device_id=device_id)

    def put(self, request, *args, **kwargs):

        serializer = PostureSerializer(data=request.data, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)