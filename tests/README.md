# Setup mock server for local debug
### Run server
```shell
cd /my/project/
export PYTHONPATH="${PYTHONPATH}:."
poetry run python mock_server/server.py
```
### Set environment variable
```shell
export MOCK_SERVER=True
```

# Running Tests

### Via PyCharm
- Confirm that PyCharm has been configured correctly: project interpreter and environment variables
- Navigate to any of the `test_<number>` files and use the PyCharm UI to run the test
It should pass first time.

### Via CLI

```shell
cd /my/project/
poetry run python -m pytest
```
