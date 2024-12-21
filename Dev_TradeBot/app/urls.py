from django.urls import path, include
from .views import MasterListCreateView, MasterRetriveUpdateDistroyView, MasterListView, testview
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'masters_list', MasterListView, basename='master_list')
# router.register(r'testview', testview, basename='testview')

urlpatterns = [
    path('master/',MasterListCreateView.as_view()),
    path('master/<pk>',MasterRetriveUpdateDistroyView.as_view()),
    path('test', testview.as_view({'get': 'list', 'post': 'create_user'})),
    path('create_master', MasterListView.as_view({'post': 'create'})),
    # path('create_child', )


#     # path('detail/<int:pk>/', views.post_detail, name='post_detail'),
#     # path('update/<int:pk>/', views.post_update, name='post_update'),
#     # path('delete/<int:pk>/', views.post_delete, name='post_delete'),
]