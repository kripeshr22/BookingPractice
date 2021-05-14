from django.urls import path
from .views import RoomList, BookingList, BookingView

# Declare our app names
APP_NAME = 'hotel'

urlpatterns = [
    path('roomlist/', RoomList.as_view(), name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('bookview/', BookingView.as_view(), name='BookingView')
]