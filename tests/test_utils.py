"""qsdfqsdfqsdf."""

from s4gpy.s4gpy import S4GAPI


class TestUtils:
    """qsdfqsdfqsdf."""

    def testing(self):
        api = S4GAPI("user1", "user")
        users = api.get_user_api().get_users()
        watches = users[0].all_watches()
        print(watches)
