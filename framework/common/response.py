import re


class ResponseModel:
    """
    Represents an abstract response
    """

    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.json = response

    @property
    def charging_state_name(self):
        msg = self.json.get("success")
        result = re.findall("State .* to ([A-Z])", msg)[0]
        return result
