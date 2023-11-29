from rest_framework import serializers
from .models import Genre, MovieType, Cinema, CinemaRoom, Movie, Showday, Customer, Ticket, Discount, Verifier, VerifierDevice, VerifierDeviceType, RoomSeat
class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
        extra_kwargs = {
            "description": {
                "required": False,
                "allow_blank": True
            }
        }


class MovieTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieType
        fields = "__all__"
        extra_kwargs = {
            "description": {
                "required": False,
                "allow_blank": True
            }
        }

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = "__all__"
        extra_kwargs = {
            "description": {
                "required": False,
                "allow_blank": True
            }
        }

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

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class VerifierDeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifierDeviceType
        fields = "__all__"

class VerifierDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerifierDevice
        fields = "__all__"

class VerifierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verifier
        fields = "__all__"

class RoomSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomSeat
        fields = "__all__"


