from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView

from .models import Genre, MovieType, Cinema, CinemaRoom, Movie, RoomSeat, Showday, Customer, Ticket, Verifier, VerifierDevice, VerifierDeviceType
from .serializers import GenreSerializer, MovieTypeSerializer, CinemaSerializer, CinemaRoomSerializer, MovieSerializer, RoomSeatSerializer, ShowdaySerializer, CustomerSerializer, TicketSerializer, VerifierDeviceSerializer, VerifierDeviceTypeSerializer, VerifierSerializer
# Create your views here.
class GenreView(ListCreateAPIView):
    '''GenreView is a class-based view that inherits from ListCreateAPIView.'''
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    def get(self, request, *args, **kwargs):
        '''This overides the default get method for the genres view'''
        genres = Genre.objects.all()
        genres_data = GenreSerializer(genres, many=True)
        return Response(data=genres_data.data, status=200)

class MovieTypeView(ListCreateAPIView):
    queryset = MovieType.objects.all()
    serializer_class = MovieTypeSerializer
    def get(self, request, *args, **kwargs):
        movie_types = MovieType.objects.all()
        movie_types_data = MovieTypeSerializer(movie_types, many=True)
        return Response(data=movie_types_data.data, status=200)


class CinemaView(ListCreateAPIView):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()
    def get(self, request, *args, **kwargs):
        cinemas = Cinema.objects.all()
        cinemas_data = CinemaSerializer(cinemas, many=True)
        return Response(data=cinemas_data.data, status=200)

class CinemaRoomView(ListCreateAPIView):
    serializer_class = CinemaRoomSerializer
    queryset = CinemaRoom.objects.all()
    def get(self, request, *args, **kwargs):
        cinema_rooms = CinemaRoom.objects.all()
        cinema_rooms_data = CinemaRoomSerializer(cinema_rooms, many=True)
        return Response(data=cinema_rooms_data, status=200)

class MovieView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    def get(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        movies_data = MovieSerializer(movies, many=True)
        return Response(data=movies_data.data, status=200)

class ShowdayView(ListCreateAPIView):
    queryset = Showday.objects.all()
    serializer_class = ShowdaySerializer
    def get(self, request, *args, **kwargs):
        showdays = Showday.objects.all()
        showdays_data = ShowdaySerializer(showdays, many=True)
        return Response(data=showdays_data.data, status=200)


class CustomerView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        customers_data = CustomerSerializer(customers, many=True)
        return Response(data=customers_data.data, status=200)


class TicketView(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    def get(self, request, *args, **kwargs):
        tickets = Ticket.objects.all()
        tickets_data = TicketSerializer(tickets, many=True)
        return Response(data=tickets_data.data, status=200)

class RoomSeatView(ListCreateAPIView):
    queryset = RoomSeat.objects.all()
    serializer_class = RoomSeatSerializer
    def get(self, request, *args, **kwargs):
        room_seats = RoomSeat.objects.all()
        room_seats_data = RoomSeatSerializer(room_seats, many=True)
        return Response(data=room_seats_data.data, status=200)

class VerifierDeviceTypeView(ListCreateAPIView):
    queryset = VerifierDeviceType.objects.all()
    serializer_class = VerifierDeviceTypeSerializer
    def get(self, request, *args, **kwargs):
        verifier_device_types = VerifierDeviceType.objects.all()
        verifier_device_types_data = VerifierDeviceTypeSerializer(verifier_device_types, many=True)
        return Response(data=verifier_device_types_data.data, status=200)

class VerifierDeviceView(ListCreateAPIView):
    queryset = VerifierDevice.objects.all()
    serializer_class = VerifierDeviceSerializer
    def get(self, request, *args, **kwargs):
        verifier_devices = VerifierDevice.objects.all()
        verifier_devices_data = VerifierDeviceSerializer(verifier_devices, many=True)
        return Response(data=verifier_devices_data.data, status=200)

class VerifierView(ListCreateAPIView):
    queryset = Verifier.objects.all()
    serializer_class = VerifierSerializer
    def get(self, request, *args, **kwargs):
        verifiers = Verifier.objects.all()
        verifiers_data = VerifierSerializer(verifiers, many=True)
        return Response(data=verifiers_data.data, status=200)
