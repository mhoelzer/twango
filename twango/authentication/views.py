from django.shortcuts import render, reverse, HttpResponseRedirect
from twango.authentication.forms import LoginForm
from django.contrib.auth import authenticate, login


def login_view(request):
    html = "../templates/generic.html"
    header = "Login"
    form = None
    button_value = "Login, buddy!"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            # data = form.cleaned_data.get()
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", "/"))
    else:
        form = LoginForm()
    return render(request, html, {"header": header, "form": form,
                                  "button_value": button_value})
