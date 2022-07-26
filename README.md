# Prerequisites
It is assumed that you are running tests on the Linux operating system.

Possible options includes:
- Linux desktop (Mint Cinnamon recommended)
- Windows 10/11 + WSL
- Windows 10/11 + Virtual machine
- Mac OS

### WSL setup on Windows
- Installation process https://pureinfotech.com/install-windows-subsystem-linux-2-windows-10/
- X-server setup to run tests in browser GUI  https://gist.github.com/KirillY/bc4253edfd62b27c452d01595d19efce
After x-server is set, you might also need to enable `AUT_IS_INSIDE_WSL` environment variable or similar to set `DISPLAY` variable inside WSL

### Credentials
You will sometimes need credentials to actually run the tests. They could be environment variables set up in CLI or PyCharm or in Docker section below.

# Local Machine Installation & Configuration

## Version control setup

### Generate Git ssh key
- ref. https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key
```
cd ~/.ssh
ls # check if already existed
ssh-keygen -t ed25519
```
### Add key to github
Navigate settings::ssh keys::add ssh key
Paste content of
```
cat ~/.ssh/id_ed25519.pub
```
### Use ssh address instead of http when clone or pull
```
git clone git@github.com:Orgname/repo-name.git # first time
git remote set-url origin  git@github.com:Orgname/repo-name.git # change
git pull # should work without any prompt
```

### Workflow to work with remote VCS repo
- Setup github key (see above)
- Clone the repository `git clone git@github.com:pythonqacourse/python-ui-framework.git`
- Create a branch and checkout into newly created branch: `git checkout -b namesurname/22-hw-checkboxes`
- Create a folder `/tests/namesurname/`
- Create a file(s) in `python-ui-framework/tests/namesurname/` and `python-ui-framework/framework` Add your code into file `test_22_hw.py`
- Check status and add/remove files from index (or use Pycharm Commit tab UI)
- Commit the changes: `git commit -am “message”`
- Fetch code from remote and merge it into local: `git pull origin main`
- Update remote  `git push --set-upstream origin namesurname/22-hw-checkboxes`
- Open https://github.com/pythonqacourse/python-ui-framework in your browser and hit Create a PR button (there should be notification for your branch)
- Please do not merge your PR without a review! (we cannot enable branch protection in a free github organizations tariff)

## Local testing environment setup
### Pip

Even though the package management for this repo is handled by Poetry, `pip` is still required to download and
configure Python modules. To install pip:

```shell
sudo apt update
sudo apt install python3-pip
```

To check this has been installed correctly, simply run:

```shell
pip --help
```

To verify you have the latest version installed, run:

```shell
pip --version
pip 21.2.4
```

If an older version is installed, upgrade by running:

```shell
pip install --upgrade pip
```

### Pyenv

Pyenv is used to easily control the versions of Python being used across different projects and repositories.
To install pyenv:

```shell
sudo apt install -y make build-essential \
                         libssl-dev \
                         zlib1g-dev \
                         libbz2-dev \
                         libreadline-dev \
                         libsqlite3-dev \
                         wget \
                         curl \
                         llvm \
                         libncurses5-dev \
                         libncursesw5-dev \
                         xz-utils \
                         tk-dev \
                         libffi-dev \
                         liblzma-dev \
                         python-openssl \
                         git
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

Ensure to restart your terminal after performing the above. To check this has been installed correctly, simply run:

```shell
pyenv --help
```

Please ensure to install the `pyenv-update` plugin so that it can be updated from the command line. To do this:

```shell
git clone https://github.com/pyenv/pyenv-update.git $(pyenv root)/plugins/pyenv-update
```

This will allow `pyenv` to be updated by running the following. It is important to do this as `pyenv` caches the
versions of Python available and so major and/or minor patches may not appear available to use without doing this.

```shell
pyenv update
```

This repository uses Python 3.9, so to install the latest version of that via `pyenv`:

```shell
pyenv install -v 3.9.7
```

This will take a few minutes as it builds Python from source. To then use this version of Python going forward:

```shell
pyenv local 3.9.7
pyenv global 3.9.7
```

To confirm the correct python version is being used, run the following command:

```shell
python --version
Python 3.9.7
```

To confirm the correct python version is being used by pyenv, run the following command:

```shell
pyenv version
3.9.7 (set by <directory>/pipeline-testing/.python-version)
```

### Poetry

The project is managed by [Poetry](https://python-poetry.org/). To install poetry, please follow the
[official guide](https://python-poetry.org/docs/).

Once Poetry is installed, to create the virtual environment and install the necessary packages, run the following
command from the root of this repo:

```shell
poetry config virtualenvs.in-project true
poetry install
```

This should create a `.venv` directory at the root of the repo.

### PyCharm

After opening the `my-project` repo as a project inside PyCharm, it needs attaching as a standalone project
within PyCharm. This allows it to be assigned its own Python interpreter (i.e. the virtual environment created by
Poetry above). To do this:

- Click `File -> Open...`
- Select the `my-project` directory
- Click `OK`
- Select the `Attach` option to attach this as an additional project

Once done, the `my-project` directory in the `Project` pane should be bolded.

To configure the Python interpreter for the `my-project` project:

- Open the PyCharm settings dialog (`Ctrl+Alt+S`)
- Expand the `Project` caret in the pane on the left-hand side
- Select `Python Interpreter`
- Select `my-project`
- Click the cog on the right-hand side of the dialog
- Select `Show All...`
- Click `+` to add a new interpreter
- Select the `Existing Environment` radio button
- Click the `...` button
- Navigate to `my-project/.venv/bin/python`
- Click `OK`
- Rename the new interpreter to `my-project` (for easier traceability)
- Click `OK`
- Click `Apply`

This should have correctly configured the `my-project` project to use the Python interpreter
created by Poetry. To confirm:

- Open any Python file in the `my-project` project
- Expand the `Imports` section at the top of the file
- All imports should be recognised and not underlined in red

### Environment Variables configuration in Pycharm

Please ensure to read through all the environment variables [defined here](./framework/common/env_vars.py)
to understand what they control. Default configurations for pytest can be setup so that these do not
need adding each time you run a specific test in PyCharm:

- Click `Run -> Edit Configurations...`
- Click `Edit configuration templates...`
- Expand the `Python` option on the left-hand side
- Click `pytest`
- Add the necessary environment variables here so all new pytest configurations inherit them for free

### VSCode

If you have Pycharm Community edition, you cannot work with WSL. One of the option might be using VSCode IDE.
To setup VScode:
- Install WSL extention if working with WSL https://code.visualstudio.com/docs/remote/wsl
- Setup python interpreter https://code.visualstudio.com/docs/python/environments
For that:
- hit `Ctrl+Shift+P` > enter `Python: Select Interpreter` > select `Enter interpreter path` > Find your interpreter
You can figure out interpreter path by using command `poetry run which python`


### Pre-commit checks

The `pre-commit` module is used to ensure the code in this repo adheres to a set of coding standards on each and every
commit. To setup the `pre-commit` hooks, run the following (this only needs doing once):

```shell
poetry run pre-commit install --install-hooks
```

Before committing code, it is recommended that you run the following command to see if any changes have caused the
static code analysis tools to highlight an issue:

```shell
poetry run pre-commit run --all-files
```


# Run tests
See detailed instructions in the `/tests/*/README.md` files

## Via Pycharm
Confirm that the project has been installed and PyCharm project interpreter, running configuration and environment variables has been configured correctly.
Use the PyCharm UI to run the test, and it should pass first time. Pycharm is automatically put root folder into `sys.path`, which updates `PYTHONPATH` and prevents ImportError

## Via CLI
By using `python -m` we are adding root to `sys.path` see https://stackoverflow.com/questions/36022892/how-to-know-if-docker-is-already-logged-in-to-a-docker-registry-server
- `poetry run python -m pytest [OPTIONS]` will temporarily activate specific environment
- `poetry shell` will permanently activate environment, then we could run `python -m pytest [OPTIONS]`



