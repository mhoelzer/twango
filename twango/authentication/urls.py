# from backend_django_recipes.models import Author, Recipes
from django.urls import path
from twango.authentication.views import (login_view)

# admin.site.register(Author)
# admin.site.register(Recipes)


urlpatterns = [
    path("login/", login_view),
]
