from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from akbars_backend.serializers import *


# create models
class WorkingRoomCreate(generics.CreateAPIView):
    serializer_class = WorkingRoomSerializer


class ResidentialHouseCreate(generics.CreateAPIView):
    serializer_class = ResidentialHouseSerializer


# get all models
class WorkingRoomList(generics.ListAPIView):
    serializer_class = WorkingRoomSerializer
    queryset = WorkingRoom.objects.all()


class ResidentialHouseList(generics.ListAPIView):
    serializer_class = ResidentialHouseSerializer
    queryset = ResidentialHouse.objects.all()


# get one model
class WorkingRoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkingRoomSerializer
    queryset = WorkingRoom.objects.all()


class ResidentialHouseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ResidentialHouseSerializer
    queryset = ResidentialHouse.objects.all()


class BookingRoomMethods(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        booked = BookingWorkingRoom.objects.all()
        serializer = BookingWorkingRoomSerializer(booked, many=True)
        return Response(serializer.data)

    def post(self, request):
        room = PostBookingWorkingRoomSerializer(data=request.data)
        if room.is_valid():
            room.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)


class BookingHouseMethods(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        booked = BookingResidentialHouse.objects.all()
        serializer = BookingResidentialHouseSerializer(booked, many=True)
        return Response(serializer.data)

    def post(self, request):
        house = PostBookingResidentialHouseSerializer(data=request.data)
        if house.is_valid():
            house.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)
