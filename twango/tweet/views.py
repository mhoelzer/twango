from django.shortcuts import render, reverse, HttpResponseRedirect
# from twango.twitteruser.models import TwitterUser
from twango.tweet.models import Tweet
from twango.tweet.forms import (TwangForm)
from django.contrib.auth.decorators import login_required


@login_required()
def twang_view(request):
    html = "../templates/generic.html"
    header = "Twang awayng!"
    form = None
    button_value = "Post your twang!"
    if request.method == "POST":
        form = TwangForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                # figureout username
                username=data["username"],
                twang=data["twang"],
                date=data["date"]
            )
        return HttpResponseRedirect(reverse("homepage"))
    else:
        form = TwangForm()
    return render(request, html, {"header": header, "form": form,
                                  "button_value": button_value})
