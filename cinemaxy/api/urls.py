from django.urls import path
from .views import GenreView, MovieTypeView, CinemaView, CinemaRoomView, MovieView, RoomSeatView, ShowdayView, CustomerView, TicketView, VerifierDeviceTypeView, VerifierDeviceView, VerifierView
urlpatterns = [
    path("genres", GenreView.as_view(), name="genres"),
    path("movie-types",  MovieTypeView.as_view(), name="movie-types"),
    path("cinemas", CinemaView.as_view(), name="cinemas"),
    path("tickets", TicketView.as_view(), name="tickets"),
    path("cinema-rooms", CinemaRoomView.as_view(), name="cinema-rooms"),
    path("seat", RoomSeatView.as_view(), name="seat"),
    path("movies", MovieView.as_view(), name="movies"),
    path("showdays", ShowdayView.as_view(), name="showdays"),
    path("customers", CustomerView.as_view(), name="customers"),
    path("verifier-device-types", VerifierDeviceTypeView.as_view(), name="verifier-device-types"),
    path("verifier-devices", VerifierDeviceView.as_view(), name="verifier-devices"),
    path("verifiers", VerifierView.as_view(), name="verifiers"),
]
