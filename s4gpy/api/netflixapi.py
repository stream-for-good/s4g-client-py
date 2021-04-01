from munch import munchify

from s4gpy.api.utils import expand_links


class NetflixAPI:
    """This class wraps the netflix-api."""

    def __init__(self, session):
        """Initialize a new NetflixAPI.

        It works by inheriting from the session object of a S4GAPI.
        """
        self.session = session

    def get_root(self):
        """get the root of the netflix api"""


        netflix_links = self.session.get("/api/netflix").json()
        expand_links(self.session, netflix_links)
        return munchify(netflix_links)
