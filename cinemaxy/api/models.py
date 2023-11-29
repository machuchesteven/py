from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    def __repr__(self) -> str:
        return f"{self.name}\n"

class MovieType(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    def __str__(self) -> str:
        return self.name

class Cinema(models.Model):
    name = models.CharField(max_length=50, unique=True)
    location = models.CharField(max_length=50)
    info = models.TextField()

class CinemaRoom(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    number = models.IntegerField() #start from 1
    code = models.CharField(max_length=10, unique=True)
    is_open = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.cinema.name} {self.number} {self.code}"

class RoomSeat(models.Model):
    room = models.ForeignKey(CinemaRoom, on_delete=models.CASCADE)
    row = models.CharField(max_length=5)
    column = models.PositiveSmallIntegerField()
    is_whole = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.room.cinema.name}: {self.room.number} {self.room.code} {self.row}{self.column}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField(null=True, blank=True, default=None)
    trailer = models.TextField()
    cover = models.ImageField(null=True, blank=True, upload_to="covers")
    release_date = models.DateField(null=True, blank=True)
    runtime = models.PositiveIntegerField() # duration in minutes
    movie_type = models.ForeignKey(MovieType, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self) -> str:
        return f"Title: {self.title}\nReleased: {self.release_date}\n{self.description}"

class Showday(models.Model):
    day = models.DateField()
    poster = models.ImageField(null=True, blank=True, upload_to="posters")
    def __str__(self) -> str:
        return f"{self.day}"

class Customer(models.Model):
    phone = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    customer_type = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=255)

class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now=True)
    showday = models.ForeignKey(Showday, on_delete=models.DO_NOTHING)
    is_used = models.BooleanField(default=False)
    code = models.CharField(max_length=255)
    seat = models.ForeignKey(RoomSeat, on_delete=models.DO_NOTHING)
    def __str__(self) -> str:
        return "Ticket %s" % self.customer.name

class Discount(models.Model):
    name = models.CharField(max_length=50)
    start = models.DateTimeField()
    ends = models.DateTimeField()
    percentage = models.DateTimeField()

class VerifierDeviceType(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

class VerifierDevice(models.Model):
    device_type = models.ForeignKey(VerifierDeviceType, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.SET_NULL, blank=True, null=True)
    code = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

class Verifier(models.Model):
    device_type = models.ForeignKey(VerifierDeviceType, on_delete=models.SET_NULL, blank=True, null=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Offer(models.Model):
    name = models.CharField(max_length=50)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    starts = models.DateTimeField()
    ends = models.DateTimeField()
    # poster = models.ImageField()
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self) -> str:
        return self.name