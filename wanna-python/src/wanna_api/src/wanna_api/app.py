import logging
import os

import django
from django.core.asgi import get_asgi_application
from django.http import JsonResponse
from wanna_core.db import DBAuth, Neo4JDatabase

LOG = logging.getLogger(__name__)

_HOME_MESSAGE = "Hello, from the async Wanna API's home endpoint 🏠!"
_URI = os.environ["WANNA_DB_URI"]

_AUTH = DBAuth(os.environ["WANNA_DB_USERNAME"], os.environ["WANNA_DB_PASSWORD"])

os.environ["DJANGO_SETTINGS_MODULE"] = "wanna_api.settings"

django.setup()
app = get_asgi_application()


async def home(request):
    """Basic Home Endpoint."""
    return JsonResponse({"message": _HOME_MESSAGE})


async def create_account(request):
    """Create Account Endpoint."""
    if request.method == "POST":
        # Unpack data and structure for database insertion
        data = request.body

        # Add our user data to our neo4j database as a new user node
        database = Neo4JDatabase(_URI, _AUTH)
        database.create_user(data["username"], data["password"])

        # Return JSON response that our account was created
        msg = f"Account for user: {data['username']}"
        LOG.info(msg)
        return JsonResponse({"message": "creating account!"})
    else:
        msg = f"Unsupported request type: {request.method} for this endpoint!"
        LOG.warning(msg)
        return JsonResponse({"error": msg})
