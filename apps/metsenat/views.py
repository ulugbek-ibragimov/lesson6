from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication
from apps.metsenat.models import Homiy, Talaba, TalabaVaHomiy
from apps.metsenat.serializers import HomiySerializer, TalabaSerializer, TalabaDetailSerializer
from django_filters import rest_framework as filters
class HomiyList(ListAPIView):
    queryset = Homiy.objects.all()
    serializer_class = HomiySerializer
    permission_classes = [IsAdminUser]
    #authentication_classes = [TokenAuthentication]
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'status',
        'homiylik_summa',
    )


class HomiyRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Homiy.objects.all()
    serializer_class = HomiySerializer
    #authentication_classes = [TokenAuthentication]

class TalabaListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Talaba.objects.all()
    serializer_class = TalabaSerializer
    #authentication_classes = [TokenAuthentication]

class TalabaRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Talaba.objects.all()
    serializer_class = TalabaDetailSerializer
    #authentication_classes = [TokenAuthentication]

    # def get_queryset(self):
    #     return Talaba.objects.get(pk=self.kwargs.get('pk'))
