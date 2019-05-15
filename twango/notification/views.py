from django.shortcuts import render, reverse, HttpResponseRedirect
from twango.notification.forms import NotificationForm
from django.contrib.auth.models import User
from twango.notification.models import Notification
from django.contrib.auth.decorators import login_required


# maybe in twitteruser, add editable=True in the model
@login_required()
def notification_view(request):
    html = "../templates/notifications.html"
    form = None
    # button_value = "Signup for your new account, buddy!"
    # if request.method == "POST":
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         user = User.objects.create_user(
    #             username=data["username"], password=data["password"])
    #             # data["username"], data["email"], data["password"])
    #         login(request, user)
    #         TwitterUser.objects.create(
    #             display_name=data["display_name"],
    #             # bio=data["bio"],
    #             user=user
    #         )
    #         return HttpResponseRedirect(reverse("home"))
    # else:
    #     form = SignupForm()
    # return render(request, html, {"form": form})
    notification = Notification.objects.all()
    return render(request, html, {"form": notification})

    # maybe make it so it deletes once you check and go to this form? no boolean?
