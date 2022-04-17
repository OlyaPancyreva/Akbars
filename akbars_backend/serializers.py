from rest_framework import serializers
from akbars_backend.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name')


class ResidentialHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidentialHouse
        fields = '__all__'


class WorkingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingRoom
        fields = '__all__'


class BookingResidentialHouseSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    residential_house = ResidentialHouseSerializer()

    class Meta:
        model = BookingResidentialHouse
        fields = '__all__'


class BookingWorkingRoomSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    working_room = WorkingRoomSerializer()

    class Meta:
        model = BookingWorkingRoom
        fields = '__all__'


class PostBookingResidentialHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingResidentialHouse
        fields = '__all__'


class PostBookingWorkingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingWorkingRoom
        fields = '__all__'
