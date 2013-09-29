from models import Hotel, Type

from rest_framework import serializers

class HotelSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Hotel
		fields =('id','title','favorite','description','category','timestamp','logoHotel','imagenHotel','latitud','longitud')
class TypeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
			model = Type
			fields = ('id','title',)