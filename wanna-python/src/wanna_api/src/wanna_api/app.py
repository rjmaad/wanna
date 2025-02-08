import logging
import os

import django
from django.core.asgi import get_asgi_application
from django.http import JsonResponse
from neo4j import GraphDatabase

from wanna_core.db import DBAuth

LOG = logging.getLogger(__name__)

_HOME_MESSAGE = "Hello, from the async Wanna API's home endpoint 🏠!"
_URI = os.environ["WANNA_DB_URI"]

_AUTH = DBAuth(os.environ["WANNA_DB_USERNAME"], os.environ["WANNA_DB_PASSWORD"])

os.environ["DJANGO_SETTINGS_MODULE"] = "wanna_api.settings"

django.setup()
app = get_asgi_application()


def create_user(tx, username, password):
    query = "CREATE (p:User {username: $username, password: $password})"
    tx.run(query, username=username, password=password)


async def home(request):
    """Basic Home Endpoint."""
    return JsonResponse({"message": _HOME_MESSAGE})


async def create_account(request):
    """Create Account Endpoint."""
    if request.method == "POST":
        # Unpack data and structure for database insertion
        data = request.body

        # Add our user data to our neo4j database as a new user node
        # TODO: clean this stuff up and move it into new library ``wanna_core``
        with GraphDatabase.driver(_URI, auth=_AUTH) as driver:
            driver.verify_connectivity()
            with driver.session() as session:
                session.execute_write(create_user, data["username"], data["password"])

        # Return JSON response that our account was created
        msg = f"Account for user: {data['username']}"
        LOG.info(msg)
        return JsonResponse({"message": "creating account!"})
    else:
        msg = f"Unsupported request type: {request.method} for this endpoint!"
        LOG.warning(msg)
        return JsonResponse({"error": msg})
