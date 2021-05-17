from django.urls import path
from .views import RoomListView, BookingList, RoomDetailView, BookingView

# Declare our app names
APP_NAME = 'hotel'

urlpatterns = [
    path('roomlist/', RoomListView, name='RoomList'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('bookview/', BookingView.as_view(), name='BookingView'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),]