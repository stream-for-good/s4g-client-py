"""qsdfqsdfqsdf."""

from s4gpy.s4gpy import S4GAPI
from s4gpy.api.companyapi import CompanyAPI
from s4gpy.s4gsession import S4GSession


class TestUtils:
    """qsdfqsdfqsdf."""

    def testing(self):

        from s4gpy.s4gpy import S4GAPI
        from s4gpy.api.companyapi import CompanyAPI
        from s4gpy.s4gsession import S4GSession
        api = CompanyAPI(S4GSession(prefix_url=f'http://localhost:5000/', access_token=""))
        api.get_root().companies()
