from framework.common.client import ApiClient
from framework.common.response import ResponseModel


class ChargingPath:
    """Represent all resources under /ev/charging"""

    def __init__(self, api_client: ApiClient):
        self.client = api_client

    def put(self, trigger) -> ResponseModel:
        """Set charging state"""
        body = {"trigger": trigger}
        response = self.client.custom_request("PUT", path="/ev/charging", json=body)
        return ResponseModel(status=response.status_code, response=response.json())

    def connect(self):
        """Trigger connect"""
        return self.put("connect")

    def disconnect(self):
        """Trigger disconnect"""
        return self.put("disconnect")

    def start(self):
        """Trigger start"""
        return self.put("start")

    def stop(self):
        """Trigger stop"""
        return self.put("stop")

    def error(self):
        """Trigger error"""
        return self.put("error")

    def non_existent_trigger(self):
        """Should cause client side error"""
        return self.put("whatever")
