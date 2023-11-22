from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country_code = models.CharField(max_length=5, blank=True, null=True)

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)

class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)


class Review(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True, null=True)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)

class Pokemon(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    birth_date=models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class PokemonCategory(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class PokemonOwner(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
