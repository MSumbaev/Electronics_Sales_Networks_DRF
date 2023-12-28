from django.urls import path

from sales_network.apps import SalesNetworkConfig
from sales_network.views import ProductCreateApiView, ProductListApiView, ProductRetrieveApiView, ProductUpdateApiView, \
    ProductDeleteApiView, NetworkElementCreateApiView, NetworkElementListApiView, NetworkElementRetrieveApiView, \
    NetworkElementUpdateApiView, NetworkElementDeleteApiView

app_name = SalesNetworkConfig.name

urlpatterns = [
    path('product/create/', ProductCreateApiView.as_view(), name='product_create'),
    path('product/list/', ProductListApiView.as_view(), name='product_list'),
    path('product/detail/<int:pk>/', ProductRetrieveApiView.as_view(), name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateApiView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteApiView.as_view(), name='product_delete'),

    path('network_element/create/', NetworkElementCreateApiView.as_view(), name='network_element_create'),
    path('network_element/list/', NetworkElementListApiView.as_view(), name='network_element_list'),
    path('network_element/detail/<int:pk>/', NetworkElementRetrieveApiView.as_view(), name='network_element_detail'),
    path('network_element/update/<int:pk>/', NetworkElementUpdateApiView.as_view(), name='network_element_update'),
    path('network_element/delete/<int:pk>/', NetworkElementDeleteApiView.as_view(), name='network_element_delete'),
]
