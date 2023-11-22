from rest_framework import serializers

from .models import *


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "password"]

class PokemonCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonCategory
        fields = "__all__"

class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

class PokemonOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonOwner
        fields = "__all__"