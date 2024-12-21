from django.shortcuts import render
from .serializer import Master, MasterSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from logic.get_latest_proxy import Proxy
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import action
# Create your views here.
import _thread
from rest_framework import pagination




class MasterListView(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

    # def get_queryset(self):
    #     pass

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serialize = self.get_serializer(page, many=True)
            return self.get_serializer(serialize.data)


    # def create(self, request, *args, **kwargs):
    #     pass
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