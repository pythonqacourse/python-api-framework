import requests
from requests import Response

from framework.common.env_vars import mock_server


class ApiClient:
    def __init__(self):
        if mock_server():
            self.url = "http://localhost:8083"
        else:
            self.url = ""

    def custom_request(self, method: str, path, **kwargs) -> Response:
        """
        A generic client for sending requests to an API.
        method: method for the new Request object: GET, OPTIONS, HEAD, POST, PUT, PATCH, or DELETE. # noqa
        url – URL for the new Request object.
        **kwargs:
            params – (optional) Dictionary, list of tuples or bytes to send in the query string for the Request. # noqa
            json – (optional) A JSON serializable Python object to send in the body of the Request. # noqa
            headers – (optional) Dictionary of HTTP Headers to send with the Request.
        """
        return requests.request(method, f"{self.url}{path}", **kwargs)
