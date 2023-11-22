from .views import *
from django.urls import path

urlpatterns = [
    path("home", HomeView.as_view(), name="home"),
    path("pokemons/", PokemonsView.as_view(), name="pokemons"),
    path("pokemons/<int:id>", PokemonsView.as_view(), name="pokemon"),
    path("countries/",CountriesView.as_view(), name="countries"),
    path("categories/",CategoriesView.as_view(), name="categories"),
    path("reviews/", ReviewsView.as_view(), name="reviews"),
    path("reviewers/", ReviwersView.as_view(), name="reviewers"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("owners/", OwnersView.as_view(), name="owners"),
    path("pokemoncategories/", PokemonCategoriesView.as_view(), name="pokemoncategories"),
    path("pokemonowners/", PokemonOwnersView.as_view(), name="pokemonowners"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("recovery/", UserRecoveryView.as_view(), name="recovery"),

    path("policy/", PolicyView.as_view(), name="policy"),
    path("about/", AboutView.as_view(), name="about"),
]
