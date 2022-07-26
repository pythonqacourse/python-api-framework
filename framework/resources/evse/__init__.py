from framework.common.client import ApiClient
from framework.resources.evse.cp import CPPath


class EVSEPath:
    """An object that represents all of the API resources within /evse"""

    def __init__(self, api_client: ApiClient) -> None:

        self.api_client = api_client
        self.cp = CPPath(api_client=api_client)
