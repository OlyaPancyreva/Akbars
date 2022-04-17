from django.urls import path

from akbars_backend.views import *

app_name = 'Backend'
urlpatterns = [
    path('room/', WorkingRoomList.as_view()),
    path('room/create', WorkingRoomCreate.as_view()),
    path('room/<int:pk>/', WorkingRoomDetailView.as_view()),

    path('house/', ResidentialHouseList.as_view()),
    path('house/create', ResidentialHouseCreate.as_view()),
    path('house/<int:pk>/', ResidentialHouseDetailView.as_view()),

    path('booking/house/', BookingHouseMethods.as_view()),

    path('booking/room/', BookingRoomMethods.as_view())
]