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

class PokemonsView(APIView):
    def get(self, request, *args, **kwargs):
        pokemons = Pokemon.objects.all()
        pokemons_data = PokemonSerializer(pokemons, many=True)
        return Response(pokemons_data.data, status=200)

class CountriesView(View):
    def get(self, request, *args, **kwargs):
        countries = Country.objects.all()
        countries_data = CountrySerializer(countries, many=True)
        return Response(countries_data.data, status=200)

class CategoriesView(APIView):
    def get(self, request, *args, **kwargs):
        cats = Category.objects.all()
        data = CategorySerializer(cats, many=True)
        return Response(data.data, status=200)
class ReviewsView(APIView):
    def get(self, request, *args, **kwargs):
        reviews = Review.objects.all()
        reviews_data = ReviewSerializer(reviews, many=True)
        return Response(reviews_data.data, status=200)

class ReviwersView(APIView):
    def get(self, request, *args, **kwargs):
        reviewers = Reviewer.objects.all()
        reviewers_data = ReviewerSerializer(reviewers, many=True)
        return Response(reviewers_data.data, status=200)

class OwnersView(APIView):
    def get(self, request, id:int|None = None, *args, **kwargs):
        if id is not None:
            owner = Owner.objects.get(id=id)
            owner_data = OwnerSerializer(owner)
            return Response(owner_data.data, status=200)
        owners = Owner.objects.all()
        owners_data = OwnerSerializer(owners, many=True)
        return Response(data=owners_data.data, status=200)

class PokemonCategoriesView(APIView):
    def get(self, request, *args, **kwargs):
        pokemon_categories = PokemonCategory.objects.all()
        pokemon_categories_data = PokemonCategorySerializer(pokemon_categories, many=True)
        return Response(pokemon_categories_data.data, status=200)

class PokemonOwnersView(APIView):
    def get(self, request, *args, **kwargs):
        pokemon_owners = PokemonOwner.objects.all()
        pokemon_owners_data = PokemonOwnerSerializer(pokemon_owners, many=True)
        return Response(pokemon_owners_data.data, status=200)

class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data={"title": "Login View"}, status=200)
    def post(self, request, *args, **kwargs):
        return Response(data={"title": "Post method execution"}, status=200)

class LogoutView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data={"title": "Logout View"}, status=200)

class CreateUserView(APIView):
    """Creation of a new user"""
    def get(self, request, *args, **kwargs):
        return Response(data={"title": "Create User Get View"}, status=200)
    def post(self, request, *args, **kwargs):
        return Response(data={"title": "Create User Post View"}, status=200)

class UserRecoveryView(APIView):
    """THis is for recovery of user accounts and passwords. """
    def get(self, request, *args, **kwargs):
        return Response(data={"title": "User Recovery Get View"}, status=200)
    def post(self, request, *args, **kwargs):
        return Response(data={"title": "User Recovery Post View"}, status=200)

class PolicyView(APIView):
    def get(self, request, *args, **kwargs):
        '''This returns the pirvacy policy and policies for usage of the project within this project'''
        return Response(data={"title": "Policy Get View"}, status=200)
    def post(self, request, *args, **kwargs):
        return Response(data={"title": "Policy Post View"}, status=200)

class AboutView(APIView):
    def get(self, request, *args, **kwargs):
        ''' This view returns information about project, including the page schema and other parts of the project'''
        return Response(data={"title": "About Get View"}, status=200)
    def post(self, request, *args, **kwargs):
        return Response(data={"title": "About Post View"}, status=200)
class ProfileView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data={"title": "Profile Get View"}, status=200)
