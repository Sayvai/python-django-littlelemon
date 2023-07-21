# Full Stack LittleLemon Restaurant Reservation System

This is a simple full-stack restaurant reservation system, which is developed using Python, and Django, as part of a Meta Back-End Developer Developer Professional Certificate program.

## Installation and Setup

### Pre-requisites

- Install Python - [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Install pipenv - `pip3 install pipenv`
- Install MySQL - [https://www.mysql.com/downloads/](https://www.mysql.com/downloads/). Or install MySQL using [Homebrew](https://brew.sh/)
- Start / Run the MySQL server
- Create a MySQL database named `littlelemon` with the following command: `CREATE DATABASE littlelemon;`

## Running the app

To install the app, clone the repository, and run the following command in the root directory of the project:

1. Create a virtual environment for the project via the terminal

```
pipenv shell
```

2. Install the dependencies via the terminal

```
pipenv install
```

3. Configure the local database environment variables in settings.py file with the appropriate credentials. The default values are as follows:

```python
# settings.py

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "littlelemon",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "USER": "admindjango",
        "PASSWORD": "employee@123!",
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"  # handles invalid or missing values from being stored in the database by INSERT and UPDATE statements
        },
    }
}
```

**Note**: if you want to create new credentials based on the example default values, then run the following SQL commands individually, from within the MySQL shell:

```sql
CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employee@123!';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'admindjango'@'localhost';
FLUSH PRIVILEGES;
```

**Note**: Also ensure your MySQL server is currently running on port 3306 (default). If not, then change the port number in the `settings.py` file.

4. Run the individual migration commands in your terminal to create the necessary database tables in the MySQL database (littlelemon):

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

5. Run the following command to start the Django development server:

```shell
python3 manage.py runserver
```

## Admin Credentials

To login to the localhost [admin](http://127.0.0.1:8000/admin) web UI interface of the app as the super user admin, use the following credentials:

```
username: admin
password: admin
```

The registered email address for the super user admin is `admin@littlelemon.com`.
