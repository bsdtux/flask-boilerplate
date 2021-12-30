# Flask Boilerplate

Flask boilerplate is a simple setup using flask-restx, flask-sqlalchemy, and
flask-migrate all wrapped up to allow for quicker coding and design without
having to remember and scaffold new projects

## Application Setup

To setup the boiler plate you will need to setup the application environment to point
to your database. Currently the only supported databases are postgres and mysql.

Edit your .env file and add the folllwing

```
DB_ENGINE=
DB_HOST=
DB_PORT=
DB_USER=
DB_PASS=
FLASK_ENV=
```

### DB_ENGINE

this is the engine that you would like to use. Currently only postgres, mysql and oracle are supported

### DB_HOST

This is the hostname for the database that you would like to use

### DB_PORT

This is the port for the database connection

### DB_USER

This will be the username the application will use for connecting to your database

### DB_PASS

This will be the password the application will use for connecting to your database

### FLASK_ENV

This is the operating environment that flask will be running in

## Run Application

To run this boilerplate you can use either make or run the the flask commands
directly

For example to run the api run one of the following commands

```shell
make run
```

or

```shell
flask run
```

## Tests

This boiler plate does contain tests. The tests can be ran by running

```shell
make test
```
