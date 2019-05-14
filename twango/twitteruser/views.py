from django.shortcuts import render, reverse, HttpResponseRedirect
from twango.twitteruser.forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from twango.twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required


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
            # data["username"], data["email"], data["password"])
            login(request, user)
            TwitterUser.objects.create(
                display_name=data["display_name"],
                # bio=data["bio"],
                user=user
            )
            return HttpResponseRedirect(reverse("home"))
    else:
        form = SignupForm()
    return render(request, html, {"header": header, "form": form,
                                  "button_value": button_value})


@login_required()
def profile_view(request):
    pass
#     html = "../templates/twitteruser.html"
#     header = "Profile of: "
#     form = None
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = User.objects.get(display_name=data["display_name"])
#             # # data["username"],data["password"])
#             # data["username"], data["email"], data["password"])
#             login(request, user)
#             TwitterUser.objects.create(
#                 display_name=data["display_name"],
#                 # bio=data["bio"],
#                 user=user
#             )
#             return User.objects
#     else:
#         form = SignupForm()
#     return render(request, html, {"header": header, "form": form})
