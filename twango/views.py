from django.shortcuts import render, reverse, HttpResponseRedirect
# ^^^ djnago has lots of imports and packages, so collect most common and put in shortcuts
# from twango.models import Recipes, Author
# from twango.forms import (
#     AuthorsForm, RecipesForm, LoginForm, SignupForm)
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from twango.tweet.models import Tweet


@login_required()
def home_view(request):
    html = "home.html"
    # items = Recipes.objects.all().order_by("title")
    # return render(request, html, {"list": items})
    twangs = Tweet.objects.all().order_by("-date")
    return render(request, html, {"twangs": twangs})
