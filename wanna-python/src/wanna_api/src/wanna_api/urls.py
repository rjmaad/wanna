from django.urls import path

from wanna_api.app import create_account, home

urlpatterns = [
    path("home/", home, name="home"),
    path("account/create/", create_account, name="create_account"),
]
