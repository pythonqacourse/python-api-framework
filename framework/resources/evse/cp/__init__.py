from framework.common.client import ApiClient
from framework.common.response import ResponseModel
from framework.models.control_pilot import ControlPilotSignal


class CPPath:
    """ElectricVehicleSupplyEquipment"""

    def __init__(self, api_client: ApiClient):
        self.client = api_client

    def get(self, method="GET", path="/evse/cp") -> ResponseModel:
        """Get control pilot signal"""
        response = self.client.custom_request(method, path=path)
        return ResponseModel(status=response.status_code, response=response.json())
