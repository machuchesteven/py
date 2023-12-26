from django.shortcuts import render
from django.db.models import Sum, Aggregate, Avg, Min, Max, Count
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


from .models import Genre, MovieType, Cinema, CinemaRoom, Movie, RoomSeat, Showday, Customer, Ticket, Verifier, VerifierDevice, VerifierDeviceType
from .serializers import GenreSerializer, MovieTypeSerializer, CinemaSerializer, CinemaRoomSerializer, MovieSerializer, RoomSeatSerializer, ShowdaySerializer, CustomerSerializer, TicketSerializer, VerifierDeviceSerializer, VerifierDeviceTypeSerializer, VerifierSerializer


# Create your views here.
class GenreView(ListCreateAPIView):
    '''GenreView is a class-based view that inherits from ListCreateAPIView.'''
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreObjectView(RetrieveUpdateAPIView):
    lookup_field = 'pk'
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class MovieTypeView(ListCreateAPIView):
    queryset = MovieType.objects.all()
    serializer_class = MovieTypeSerializer

class MovieTypeObjectView(RetrieveUpdateAPIView):
    queryset = MovieType.objects.all()
    serializer_class = MovieTypeSerializer
    lookup_field = "pk"


class CinemaView(ListCreateAPIView):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()


class CinemaObjectView(RetrieveUpdateAPIView):
    serializer_class = CinemaSerializer
    queryset = Cinema.objects.all()

class CinemaRoomView(ListCreateAPIView):
    serializer_class = CinemaRoomSerializer
    queryset = CinemaRoom.objects.all()

class CinemaRoomObjectView(RetrieveUpdateAPIView):
    serializer_class = CinemaRoomSerializer
    queryset = CinemaRoom.objects.all()

class MovieView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class MovieObjectView(RetrieveUpdateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class ShowdayView(ListCreateAPIView):
    queryset = Showday.objects.all()
    serializer_class = ShowdaySerializer

class ShowdayObjectView(RetrieveUpdateAPIView):
    queryset = Showday.objects.all()
    serializer_class = ShowdaySerializer


class CustomerView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerObjectView(RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class TicketView(ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketObjectView(RetrieveUpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class RoomSeatView(ListCreateAPIView):
    queryset = RoomSeat.objects.all()
    serializer_class = RoomSeatSerializer

class RoomSeatObjecrView(RetrieveUpdateAPIView):
    queryset = RoomSeat.objects.all()
    serializer_class = RoomSeatSerializer

class VerifierDeviceTypeView(ListCreateAPIView):
    queryset = VerifierDeviceType.objects.all()
    serializer_class = VerifierDeviceTypeSerializer

class VerifierDeviceTypeObjectView(RetrieveUpdateAPIView):
    queryset = VerifierDeviceType.objects.all()
    serializer_class = VerifierDeviceTypeSerializer


class VerifierDeviceView(ListCreateAPIView):
    queryset = VerifierDevice.objects.all()
    serializer_class = VerifierDeviceSerializer

class VerifierDeviceObjectView(RetrieveUpdateAPIView):
    queryset = VerifierDevice.objects.all()
    serializer_class = VerifierDeviceSerializer


class VerifierView(ListCreateAPIView):
    queryset = Verifier.objects.all()
    serializer_class = VerifierSerializer


class VerifierObjectView(RetrieveUpdateAPIView):
    queryset = Verifier.objects.all()
    serializer_class = VerifierSerializer


class SummaryView(APIView):
    def get(self, request, *args, **kwargs):
        count_of_genres = Genre.objects.all().count()
        genre = Genre.objects.get(id=1)
        return Response(data={"totals": {
            "genres": {"count": count_of_genres},
            "users": {"count": User.objects.all().count()},
            "cinema_rooms": CinemaRoom.objects.get(cinema=1),
        }}, status=200)