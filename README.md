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

## Database

This app uses a Postgresql database. Install your version locally such that you can access
the console using `psql`.

From here, create a new database `tracker_local`, user `tracker_user`.

Grant the user all permissions on the database and then exit the terminal prompt.

Now, enter the venv for the Django backend and active it. Then run `pip install django psycopg2`.

If you're running macOS and installing psycopg2 errors out, try running:
`env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip install psycopg2`.  
It sets the openssl version to that installed by homebrew when installing psycopg2.

### Ubunutu

For an Ubuntu system, I was just able to run

`sudo apt install postresql`

`sudo apt install python-psycopg2`

`sudo apt install libpq-dev`
