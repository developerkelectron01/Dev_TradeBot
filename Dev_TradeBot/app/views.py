from .serializer import Master, MasterSerializer
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
        if not Master.objects.filter(referal_code=ref_code).exists():
            return ref_code

class MasterListView(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = MasterFilter
    # permission_classes = [IsAuthenticated]


    # @action(methods='post')
    def create(self, request, *args, **kwargs):
        data = request.data
        print(data)
        if data['user_type'] == 0:
            add_data = {
                'referal_code': create_referral_code()
            }
            data.update(add_data)
            serializer = MasterSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif data['user_type'] == 1:
            # serializer = MasterSerializer(data=data)
            if data['child_name'] is not None and data['referal_code']:
                master_referal_code = data['referal_code']
                child_name = data['child_name']
                records = Master.objects.filter()
                # records = Master.objects.filter(referal_code=master_referal_code)
                # if records:
                #     for record in records:
                #         if not record.child_name:
                #             record.child_name = child_name
                #             record.save()
                #             print('child account Created')
                #             return Response(serializer.data, status=status.HTTP_200_OK)
                #         else:
                #             return Response({'error': 'Child account already exists'}, status=status.HTTP_400_BAD_REQUEST)
                # else:
                #     return Response({'error': 'Invalid referral code'}, status=status.HTTP_400_BAD_REQUEST)


            # print('3333')
            # serializer = MasterSerializer(data=data)
            # print(serializer)
            # # serializer = ChildSerializer(data=data)
            # if serializer.is_valid():
            #     print('valid')
            #     serializer.save()
            #     return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"error": "Invalid user type"}, status=status.HTTP_400_BAD_REQUEST)


    #
    # def update(self, request, *args, **kwargs):
    #     pass
    #
    # def destroy(self, request, *args, **kwargs):
    #     pass



    # def list(self, request, *args, **kwargs):
    #
    #     serializer_class = self.serializer_class(queryset, many=True)
    #     return Response(serializer_class.data)
    #
    #
    # def retrieve(self, request, pk=None, *args, **kwargs):
    #     queryset = Master.objects.all()
    #     master = get_object_or_404(queryset, pk=pk)
    #     serializer_class = self.serializer_class(master)
    #     return Response(serializer_class.data)

# class ChildListCreate(viewsets.ModelViewSet):
#     queryset = Child.objects.all()
#     serializer_class = ChildSerializer


class MasterListCreateView(generics.ListCreateAPIView):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

    # def get(self, request, *args, **kwargs):
    #     proxy = Proxy
    #     proxy.main(self)
    #     response = super().get(request, *args, **kwargs)
    #     return response
    #
    #
    # def create(self, serializer):
    #     proxy = Proxy
    #     proxy.main(self)
    #     serializer.save()
class MasterRetriveUpdateDistroyView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Master.objects.all()
    serializer_class = MasterSerializer


# from rest_framework import viewsets
# class MasterListView(viewsets.ModelViewSet):
#     queryset = Master.objects.all()
#     serializer_class = MasterSerializer
#
#     def create(self, request, *args, **kwargs):
#         proxy = Proxy
#         proxy.main(self)
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#



from rest_framework import viewsets

class testview(viewsets.ViewSet):
    # def setup(self, request, *args, **kwargs):
    #     pass
    # def perform
    def list(self, request, *args, **kwargs):
        return Response({'massege : Custom get action'})
    @action(detail=False, methods=['POST'])
    def create_user(self, request):
        # if request.data:
        #     print(request.data)
        #     proxy = Proxy()
        #     proxy.main()
        #     return Response({'massage': 'Proxy Started ...'})
        return Response({'massege : Custom Post action'})
    # def execute_proxy(self, request):
    #     pass


    @action(detail=True, methods=['GET'])
    def get_user(self, request, pk=None):
        return Response({'massege : Custom Get action'})


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset that provides the standard actions
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     @action(detail=True, methods=['post'])
#     def set_password(self, request, pk=None):
#         user = self.get_object()
#         serializer = PasswordSerializer(data=request.data)
#         if serializer.is_valid():
#             user.set_password(serializer.validated_data['password'])
#             user.save()
#             return Response({'status': 'password set'})
#         else:
#             return Response(serializer.errors,
#                             status=status.HTTP_400_BAD_REQUEST)
#
#     @action(detail=False)
#     def recent_users(self, request):
#         recent_users = User.objects.all().order_by('-last_login')
#
#         page = self.paginate_queryset(recent_users)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(recent_users, many=True)
#         return Response(serializer.data)