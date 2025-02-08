import os

ROOT_URLCONF = "wanna_api.urls"
DEBUG = True
SECRET_KEY = os.environ["WANNA_DJANGO_SECRET_KEY"]
