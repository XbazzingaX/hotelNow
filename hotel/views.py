# Create your views here.
from models import Hotel, Type
from rest_framework import viewsets
from .serializers import HotelSerializer, TypeSerializer


class HotelViewSet(viewsets.ModelViewSet):
	queryset = Hotel.objects.all()
	serializer_class = HotelSerializer

class TypeViewSet(viewsets.ModelViewSet):
	queryset = Type.objects.all()
	serializer_class = TypeSerializer