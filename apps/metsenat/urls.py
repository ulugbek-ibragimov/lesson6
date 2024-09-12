from django.urls import path
from apps.metsenat.views import HomiyList, HomiyRetrieveUpdateAPIView, TalabaListCreateAPIView, TalabaRetrieveUpdateAPIView

urlpatterns = [
    #path('dashboard/', ),
    path('homiy-list/', HomiyList.as_view(), name='homiy-list'),
    path('homiy-list/<int:pk>/', HomiyRetrieveUpdateAPIView.as_view(), name='homiy-detail-update'),
    path('talaba-list/',TalabaListCreateAPIView.as_view(), name='talaba-list-create'),
    path('talaba-list/<int:pk>/', TalabaRetrieveUpdateAPIView.as_view(), name='talaba-detail-update'),
]
