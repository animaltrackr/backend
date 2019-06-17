## Setup

This backend uses Python3 and Django and was performed on Linux

`git clone` repo

Can use `virtualenv` to manage your Python dependencies if you want.

Once this is installed, in the project directory `virtualenv -p python3 venv`

`source venv/bin/activate` to set your python environment. Type `deactivate` at any time to stop using this environment.

`pip install -r requirements.txt`
`pre-commit install` for pre-commit hooks and code formatting/linting.

`python manage.py runserver` to run the instance.

The site can then be hit at `localhost:8000`

