from django.shortcuts import render, reverse, HttpResponseRedirect
from twango.twitteruser.forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from twango.twitteruser.models import TwitterUser
from twango.tweet.models import Tweet


# maybe in twitteruser, add editable=True in the model
def signup_view(request):
    html = "../templates/generic.html"
    header = "Signup"
    form = None
    button_value = "Signup for your new account, buddy!"
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data["username"], password=data["password"])
            login(request, user)
            TwitterUser.objects.create(
                username=data["username"],
                display_name=data["display_name"],
                # bio=data["bio"],
                user=user
            )
            return HttpResponseRedirect(reverse("home"))
    else:
        form = SignupForm()
    return render(request, html, {"header": header, "form": form,
                                  "button_value": button_value})


def profile_view(request, username):
    html = "../templates/twitteruser.html"
    targeteduser = TwitterUser.objects.filter(username=username).first()
    targeteduser_twangs = Tweet.objects.filter(
        user=targeteduser).order_by("-date")
    num_twangs = len(targeteduser_twangs)
    # num_followers = len()
    # currentuser = TwitterUser.objects.filter(username=request.user.twitteruser).first()
    # twangs = TwitterUser.objects.all().filter(twitteruser_id=id)
    # twangs = Tweet.objects.filter(user=request.user.twitteruser)
    return render(request, html, {"targeteduser": targeteduser,
                                  "twangs": targeteduser_twangs,
                                  "num_twangs": num_twangs})
