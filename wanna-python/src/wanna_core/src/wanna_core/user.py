from shapely.geometry import Point


class User:
    """Defines a Wanna User account.

    Attributes
    ----------
    username: str
        The usersname for this user.
    password: str
        The password for this user.
        TODO: should this be a string? Where is the password encrypted/unencrypted?
    location: Point
        ``(Longitude, Latitude)`` point of our user's primary location.
    friends: List[User]
        List of this user's friends.
    events: List[Event]
        List of events this user is either hosting or attending.
    """

    def __init__(
        self,
        username: str,
        password: str,
        location: Point,
        friends: list = None,
        events: list = None,
    ):
        """Creates a Wanna User object.

        Parameters
        ----------
        username: str
            The usersname for this user.
        password: str
            The password for this user.
            TODO: should this be a string? Where is the password encrypted/unencrypted?
        location: Point
            ``(Longitude, Latitude)`` point of our user's primary location.
        friends: List[User], optional
            List of this user's friends. Default is None.
            If no friends are provided, will set as an empty list.
        events: List[Event], optional
            List of events this user is either hosting or attending. Default is None.
            If no events are provided, will set as an empty list.

        Returns
        -------
        User
        """
        # Check if friends is None, if so, just set to an empty list
        if friends is None:
            friends = []

        # Similarly check if events is None, if so, set to an empty list
        if events is None:
            events = []

        # Now we can define our base class attributes
        self.username = username
        self.password = password
        self.location = location
        self.friends = friends
        self.events = events

    @classmethod
    def from_database(cls, database):
        """Creates a new User object from a user in the database."""
        # TODO: implement this logic next
        pass
