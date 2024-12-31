from .serializer import (
    UserType, UserTypeSerializer

)
from django.contrib.messages import MessageFailure
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
# from rest_framework import filtere
from django_filters import rest_framework as filters
# from Dev_TradeBot.logic.get_latest_proxy import Proxy
from rest_framework.response import Response
from rest_framework.decorators import action
from .filter import MasterFilter
# from .models import Child
# from .serializer import ChildSerializer
import random
import string
# Create your views here.



def create_referral_code():
    while True:
        ref_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        if not UserType.objects.filter(referral_code=ref_code).exists():
            return ref_code

class MasterListCreateView(viewsets.ModelViewSet):
    queryset = UserType.objects.all()
    serializer_class = UserTypeSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = MasterFilter

    # @action(methods='post')
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        print(data)
        if int(data['user_type']) == 0:
            add_data = {
                'referral_code': create_referral_code()
            }
            data.update(add_data)
            print('3333')
            serializer = UserTypeSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif int( data['user_type']) == 1:

            if data['child_name'] != '' and data['referral_code'] != '' and data['master_id'] != '':
                print('111')
                record = UserType.objects.filter(id=data['master_id']).first()
                if record:
                    serializer = UserTypeSerializer(data=data)
                    print(serializer)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'error': 'Invalid referral code or child Name'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'enter Mater_id/child/referral code '}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Invalid user type"}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        object_id = request.query_params.get('master_id',None)
        if object_id:
            record = UserType.objects.filter(master_id=object_id)
            if record:
                return Response(UserTypeSerializer(record, many=True).data)
        else:
            return Response(UserTypeSerializer(UserType.objects.all(), many=True).data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({'message: Record Delete Successfully'}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        object_id = self.get_object()
        if request.method == 'PUT':
            print('555')
            serializer = UserTypeSerializer(instance=object_id, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PATCH':
            print('666')
            serializer = UserTypeSerializer(instance=object_id, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)








