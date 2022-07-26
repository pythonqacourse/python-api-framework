import os


def _get_env_var(name: str, default: str = ""):
    """
    Gets the value of an environment variable. If the environment variable does not exist, it throws a ValueError.

    :param name: The name of the environment variable to fetch.
    :param default: Option for setting a default value to return if the env variable is not found.
    :return: The value of an environment variable.
    """
    if name not in os.environ and not default:
        raise ValueError(f"The {name} environment variable has not been set.")
    return os.getenv(name, default)


def mock_server() -> bool:
    """
    If True starts mock server to emulate evse/ev API
    """
    return bool(_get_env_var("MOCK_SERVER") == "True")
