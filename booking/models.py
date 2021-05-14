from django.db import models

# Create your models here.

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
        return f'{self.number}, {self.category} with {self.beds} bed(s) for {self.capacity} people'
