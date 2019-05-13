from django.urls import path
from twango.twitteruser.views import (signup)

urlpatterns = [
    path("signup/", signup),
]
