from django.urls import path
from twango.tweet.views import (twang_view)


urlpatterns = [
    path("twang/", twang_view),
]
