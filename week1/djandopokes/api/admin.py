from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Category)
admin.site.register(PokemonCategory)
admin.site.register(PokemonOwner)
admin.site.register(Owner)
admin.site.register(Country)
admin.site.register(Review)
admin.site.register(Reviewer)