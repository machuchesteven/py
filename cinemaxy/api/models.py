from django.db import models

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