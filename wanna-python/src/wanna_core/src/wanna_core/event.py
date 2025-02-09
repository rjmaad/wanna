from dataclasses import dataclass
from typing import List, Union

from shapely.geometry import Point

from wanna_core.user import User


@dataclass
class Interaction:
    """Idk what this is gonna be yet, but need a way to store user interactions
    with events and it is gonna need to be some kind of class.
    """


class Event:
    """Defines a Wanna Event.

    Attributes
    ----------
    name: str
        The name of this event.
    description: str
        The description for this event.
    host: List[User]
        The host(s) for the event.
    interactions: List[Interaction]
        User interactions with this event.
    location: Point
        ``(Longitude, Latitude)`` point for the event's location.
    is_community_event: bool
        If this is a community event or not (basically public or private).
    """

    def __init__(
        self,
        name: str,
        description: str,
        host: Union[User, list],
        interactions: List[Interaction],
        location: Point = None,
        is_community_event: bool = False,
    ):
        """Creates a Wanna Event object.

        Parameters
        ----------
        name: str
            The name of this event.
        description: str
            The description for this event.
        host: Union[User, list]
            The host(s) for the event.
        interactions: List[Interaction]
            User interactions with this event.
        location: Point, optional
            ``(Longitude, Latitude)`` point for the event's location. Default is None.
        is_community_event: bool, optional
            If this is a community event or not (basically public or private).
            Default is False.

        Returns
        -------
        Event
        """
        # Just define our base class attributes
        self.name = name
        self.description = description
        self.host = [host] if isinstance(host, User) else host
        self.interactions = interactions
        self.location = location
        self.is_community_event = is_community_event

    @classmethod
    def from_database(cls, database):
        """Creates a new Event object from an Event in the database."""
        # TODO: implement this logic next
        pass
