from framework.common.client import ApiClient
from framework.resources.ev import EVPath
from framework.resources.evse import EVSEPath


class Resources:
    """An object that represents all of the API resources contained within the application"""

    def __init__(self, api_client: ApiClient) -> None:

        self.api_client = api_client
        self.ev = EVPath(api_client=api_client)
        self.evse = EVSEPath(api_client=api_client)
