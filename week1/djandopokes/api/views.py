from django.shortcuts import render, HttpResponse
from django.views import View
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Thanks for coming home!</h1>")

class DemoAPIView(APIView):
    """Demo API view"""
    def get(self, request, *args, **kwargs):
        """Gets the introductory info of the application"""
        try:
            pokemons = Pokemon.objects.all()
            return Response(data={"title": "Welcome", "pokemons": pokemons}, status=200)
        except Exception as e:
            return Response(data={"title": "welcome but pokemons does not exists yet", "pokemons": []}, status=200)
    def post(self, request, *args, **kwargs):
        return Response(data={"title": "Post method execution"}, status=200)

class PokemonsView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Pokemon View</h1>")

class CountriesView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Countries View</h1>")

class CategoriesView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Category View</h1>")

class ReviewsView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1> Review View</h1>")

class ReviwersView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1> Reviwer View</h1>")

class OwnersView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1> Owner View</h1>")

class PokemonCategoriesView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1> Pokemon Categories View</h1>")

class PokemonOwnersView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1> Pokemon Owners View</h1>")

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1> Login View</h1>")

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1> Logout View</h1>")

class CreateUserView(View):
    """Creation of a new user"""
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1> Create User View</h1>")

class UserRecoveryView(View):
    """THis is for recovery of user accounts and passwords. """
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1> User Recovery View</h1>")

class PolicyView(View):
    def get(self, request, *args, **kwargs):
        '''This returns the pirvacy policy and policies for usage of the project within this project'''
        return HttpResponse("<h1>Privacy Policy View</h1>")

class AboutView(View):
    def get(self, request, *args, **kwargs):
        ''' This view returns information about project, including the page schema and other parts of the project'''
        return HttpResponse("<h1>About Us View</h1>")
class ProfileView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("<h1>Profile View</h1>")
