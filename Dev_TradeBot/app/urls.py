from django.urls import path, include
from .views import  MasterListCreateView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'child', ChildListCreateViewSet, basename='child')
router.register(r'master_child', MasterListCreateView, basename='Create list Master/child')

urlpatterns = [

    path('', include(router.urls))
    # path('master/',MasterListCreateView.as_view()),
    # path('master/<pk>',MasterRetriveUpdateDistroyView.as_view()),
    # path('test', testview.as_view({'get': 'list', 'post': 'create_user'})),
    # path('master/', MasterListView.as_view({'post': 'create'}), name='create Master'),
    # path('masters', MasterListView.as_view({'get':'list'}), name='list master'),
    # path('master/<pk>', MasterUpdateDeleteView.as_view({'put': 'update'}), name='update delete master'),
    # path('child', ChildListCreateViewSet.as_view({'post': 'create', 'get':'list'}), name='create Child'),
    # path('childs/', ChildListCreateViewSet.as_view({'get': 'list'}), name='list Child')
    # path('child', ChildListCreateViewSet.as_view({'post': 'create'}), name='create Child'),
    # path('childs/', ChildListCreate.as_view({'get': 'list'}), name='list Child')

    # path('child/', ChildListCreateViewSet.as_view({'post': 'create', 'get': 'list'}), name='child_list_create'),

    # path('detail/<int:pk>/', views.post_detail, name='post_detail'),
    # path('update/<int:pk>/', views.post_update, name='post_update'),
    # path('delete/<int:pk>/', views.post_delete, name='post_delete'),
]
