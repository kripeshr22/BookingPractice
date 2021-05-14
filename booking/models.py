from django.db import models
from django.conf import settings

# Create your models here.

# Room model to determine the type, capacity, beds
class Room(models.Model):
    ROOM_CATEGORIES = (
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KNG', 'KING'),
        ('QWN', 'QUEEN')
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        # using f string
        return f'{self.number}: {self.category} with {self.beds} bed(s) for {self.capacity} people'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} until {self.check_out}'


