from django.urls import path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)


from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

from .views import ( CinemaObjectView, CinemaRoomObjectView, CustomerObjectView,
                    GenreObjectView, GenreView, MovieObjectView,
                    MovieTypeObjectView, MovieTypeView, CinemaView,
                    CinemaRoomView, MovieView, RoomSeatObjecrView,
                    RoomSeatView, ShowdayObjectView, ShowdayView,
                    CustomerView, SummaryView, TicketObjectView,
                    TicketView, VerifierDeviceObjectView, VerifierDeviceTypeObjectView,
                    VerifierDeviceTypeView, VerifierDeviceView,
                    VerifierObjectView, VerifierView
                    )

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Cinemaxy API",
        default_version='v1',
        description="API for Cinemaxy",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="machuchesteven@gmail.com"), public=True,
        license=openapi.License(name="BSD License"),
    )
)

urlpatterns = [
    # path('', get_schema_view(
    #     title="Cinemaxy API",
    #     description="API for Cinemaxy",
    #     version="1.0.0",
    # ), name='openapi-schema'), # depends on pyyaml and uritemplates
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),

    # for other models of the app
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), # depends on swagger
    path("docs", include_docs_urls(title="Cinemaxy API", description="API for Cinemaxy")), # depends on coreapi and coreschema
    path("genres", GenreView.as_view(), name="genres"),
    path("genre/<int:pk>", GenreView.as_view(), name="genre"),

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
    
    path("summary", SummaryView.as_view(), name="summary"),
]
