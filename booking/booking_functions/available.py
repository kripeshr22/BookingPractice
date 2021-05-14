import datetime
from booking.models import Room, Booking

def check_available(room, check_in, check_out):
    avail_list = []
    booking_list = Booking.objects.filter(room=room) # returns a query set that is of the bookings of the room we pass in
    for booking in booking_list:
        # if preexisting booking's checkin is after my checkout
        # or if existing booking's checkout is before my checkin
        if booking.check_in > check_out or booking.check_out < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    # any is opposite of all
    return all(avail_list) # returns True if all items on the list are True, else False