from framework.common.client import ApiClient
from framework.resources.ev.charging import ChargingPath


class EVPath:
    """Represents all paths under /ev"""

    def __init__(self, api_client: ApiClient) -> None:

        self.api_client = api_client
        self.charging = ChargingPath(api_client=api_client)
