"""qsdfqsdfqsdf."""

from s4gpy.s4gpy import S4GAPI
from s4gpy.api.companyapi import CompanyAPI
from s4gpy.s4gsession import S4GSession


class TestUtils:
    """qsdfqsdfqsdf."""

    def testing(self):

        from s4gpy.s4gpy import S4GAPI
        # create an API entrypoint
        api = S4GAPI("user1", "user", root_dns="stream4good.fr")
        # get the user_api
        user_api = api.get_user_api()

        # for each user
        for u in user_api.get_users():
            # get all the video she watched
            watched_videos = [w.video_id for w in u.all_watches().watches]
            # for all the thumbnails
            for t in u.all_thumbnails()["thumbnails"]:
                # only dump the informations if the user has wached the video
                if t.video_id in watched_videos:
                    print(f"{u.user.user_id};{t.row};{t.col};{t.video_id};{t.timestamp}")


        pass
