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

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField(null=True, blank=True, default=None)
    trailer = models.TextField()
    # cover = models.ImageField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    runtime = models.PositiveIntegerField() # duration in minutes
    movie_type = models.ForeignKey(MovieType, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self) -> str:
        return f"Title: {self.title}\nReleased: {self.release_date}\n{self.description}"

class Showday(models.Model):
    day = models.DateField()


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

class Verifier(models.Model):
    device_type = models.ForeignKey(VerifierDeviceType, on_delete=models.SET_DEFAULT, blank=True)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class Offer(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
