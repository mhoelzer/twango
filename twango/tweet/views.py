from django.shortcuts import render, reverse, HttpResponseRedirect
# from twango.twitteruser.models import TwitterUser
from twango.tweet.models import Tweet
from twango.tweet.forms import TwangForm
from django.contrib.auth.decorators import login_required


@login_required()
def twang_creation_view(request):
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
                username=request.user.twitteruser,
                # display_name=request.user.twitteruser,
                twang=data["twang"],
                # date=data["date"]
            )
        return HttpResponseRedirect(reverse("home"))
    else:
        form = TwangForm()
    return render(request, html, {"header": header, "form": form,
                                  "button_value": button_value})


# own twangs
def twang_view(request):
    # get all twangs and render to page
    html = "twangs.html"
    # twangs = Tweet.objects.all()
    twangs = Tweet.objects.filter()
    return render(request, html, {"twangs": twangs})


# # own and with followers
# def author_detail(request, id):
#     pass
#     html = "author_detail.html"
#     authors = Author.objects.all().filter(id=id)
#     items = Recipes.objects.all()(author_id=id)
#     return render(request, html, {"authors": authors, "recipes": items})

    # html = "list_view.html"
    # items = Recipes.objects.all().order_by("title")
    # return render(request, html, {"list": items})