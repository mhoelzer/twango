from django.shortcuts import render, reverse, HttpResponseRedirect
# ^^^ djnago has lots of imports and packages, so collect most common and put in shortcuts
# from twango.models import Recipes, Author
# from twango.forms import (
#     AuthorsForm, RecipesForm, LoginForm, SignupForm)
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from twango.tweet.models import Tweet
from twango.twitteruser.models import TwitterUser
# from twango.twitteruser.models import TwitterUser


@login_required()
def home_view(request):
    html = "home.html"
    # make it filter based on following; will have to import w/e
    # targeteduser = TwitterUser.objects.filter(username=request.user.twitteruser).first()
    twangs = Tweet.objects.filter(user=request.user.twitteruser)
    # twangs = Tweet.objects.filter(user=request.user.twitteruser).order_by("-date")
    twangs_of_followings = Tweet.objects.filter()
    # make queries list then pass list; call both then convert; lose o_b w/ list
    # twangs = Tweet.objects.filter().order_by("-date")

    # twangs = Tweet.objects.filter().order_by("-date")
    return render(request, html, {"twangs": twangs})
