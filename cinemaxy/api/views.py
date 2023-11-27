from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Genre, MovieType, Cinema, CinemaRoom, Movie, Showday, Customer, Ticket
from .serializers import GenreSerializer, MovieTypeSerializer, CinemaSerializer, CinemaRoomSerializer, MovieSerializer, ShowdaySerializer, CustomerSerializer, TicketSerializer
# Create your views here.
class GenreView(APIView):
    def get(self, request, *args, **kwargs):
        genres = Genre.objects.all()
        genres_data = GenreSerializer(genres, many=True)
        return Response(data=genres_data.data, status=200)

class MovieTypeView(APIView):
    def get(self, request, *args, **kwargs):
        movie_types = MovieType.objects.all()
        movie_types_data = MovieTypeSerializer(movie_types, many=True)
        return Response(data=movie_types_data.data, status=200)

class CinemaView(APIView):
    def get(self, request, *args, **kwargs):
        cinemas = Cinema.objects.all()
        cinemas_data = CinemaSerializer(cinemas, many=True)
        return Response(data=cinemas_data.data, status=200)

class CinemaRoomView(APIView):
    def get(self, request, *args, **kwargs):
        cinema_rooms = CinemaRoom.objects.all()
        cinema_rooms_data = CinemaRoomSerializer(cinema_rooms, many=True)
        return Response(data=cinema_rooms_data, status=200)

class MovieView(APIView):
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        movies_data = MovieSerializer(movies, many=True)
        return Response(data=movies_data.data, status=200)

class ShowdayView(APIView):
    def get(self, request, *args, **kwargs):
        showdays = Showday.objects.all()
        showdays_data = ShowdaySerializer(showdays, many=True)
        return Response(data=showdays_data.data, status=200)


class CustomerView(APIView):
    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        customers_data = CustomerSerializer(customers, many=True)
        return Response(data=customers_data.data, status=200)


class TicketView(APIView):
    def get(self, request, *args, **kwargs):
        tickets = Ticket.objects.all()
        tickets_data = TicketSerializer(tickets, many=True)
        return Response(data=tickets_data.data, status=200)