from rest_framework import serializers
from .models import Genre, MovieType, Cinema, CinemaRoom, Movie, Showday
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieType
        fields = "__all__"
    
class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = "__all__"

class CinemaRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaRoom
        fields = "__all__"

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class ShowdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Showday
        fields = "__all__"

