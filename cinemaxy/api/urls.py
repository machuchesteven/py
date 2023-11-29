from django.urls import path
from .views import CinemaObjectView, CinemaRoomObjectView, CustomerObjectView, GenreObjectView, GenreView, MovieObjectView, MovieTypeObjectView, MovieTypeView, CinemaView, CinemaRoomView, MovieView, RoomSeatObjecrView, RoomSeatView, ShowdayObjectView, ShowdayView, CustomerView, TicketObjectView, TicketView, VerifierDeviceObjectView, VerifierDeviceTypeObjectView, VerifierDeviceTypeView, VerifierDeviceView, VerifierObjectView, VerifierView
urlpatterns = [
    path("genres", GenreView.as_view(), name="genres"),
    path("genre/<int:pk>", GenreObjectView.as_view(), name="genre"),

    path("movie-types",  MovieTypeView.as_view(), name="movie-types"),
    path("movie-type/<int:pk>",  MovieTypeObjectView.as_view(), name="movie-type"),

    path("cinemas", CinemaView.as_view(), name="cinemas"),
    path("cinema/<int:pk>", CinemaObjectView.as_view(), name="cinema"),

    path("cinema-rooms", CinemaRoomView.as_view(), name="cinema-rooms"),
    path("cinema-room/<int:pk>", CinemaRoomObjectView.as_view(), name="cinema-room"),

    path("tickets", TicketView.as_view(), name="tickets"),
    path("ticket/<int:pk>", TicketObjectView.as_view(), name="ticket"),

    path("seats", RoomSeatView.as_view(), name="seats"),
    path("seat/<int:pk>", RoomSeatObjecrView.as_view(), name="seat"),

    path("movies", MovieView.as_view(), name="movies"),
    path("movie/<int:pk>", MovieObjectView.as_view(), name="movie"),

    path("showdays", ShowdayView.as_view(), name="showdays"),
    path("showday/<int:pk>", ShowdayObjectView.as_view(), name="showday"),

    path("customers", CustomerView.as_view(), name="customers"),
    path("customer/<int:pk>", CustomerObjectView.as_view(), name="customer"),

    path("verifier-device-types", VerifierDeviceTypeView.as_view(), name="verifier-device-types"),
    path("verifier-device-type/<int:pk>", VerifierDeviceTypeObjectView.as_view(), name="verifier-device-type"),

    path("verifier-devices", VerifierDeviceView.as_view(), name="verifier-devices"),
    path("verifier-device/<int:pk>", VerifierDeviceObjectView.as_view(), name="verifier-device"),

    path("verifiers", VerifierView.as_view(), name="verifiers"),
    path("verifier/<int:pk>", VerifierObjectView.as_view(), name="verifier"),
]
