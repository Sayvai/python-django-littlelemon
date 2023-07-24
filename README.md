# Full Stack LittleLemon Restaurant Reservation System

This is a simple full-stack restaurant reservation system, which is developed using Python, and Django, as part of a Meta Back-End Developer Developer Professional Certificate program.

## Installation and Setup

### Pre-requisites

- Install Python - [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Install pipenv - `pip3 install pipenv`
- Install MySQL - [https://www.mysql.com/downloads/](https://www.mysql.com/downloads/). Or install MySQL using [Homebrew](https://brew.sh/)
- Start / Run the MySQL server
- Create a MySQL database named (for example, `littlelemon_sayvai`) with the following command: `CREATE DATABASE littlelemon_sayvai;`

## Running the app

To install the app, clone the repository, and run the following command in the root directory of the project:

1. Clone the repository

```
git clone <INSERT HTTPS / SSH URL>
```

ℹ️ - This step only needs to be done once, when you first install the app.

2. cd into the project directory. For example:

```
cd littlelemon
```

3. Create a virtual environment for the project via the terminal

```
pipenv shell
```

4. Install the dependencies via the terminal

```
pipenv install
```

ℹ️ - This step only needs to be done once, when you first install the app.

5. Configure the local database environment variables in settings.py file with the appropriate credentials. The default values are as follows:

```python
# settings.py

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "littlelemon_sayvai", # 👈 AMEND DATABASE NAME HERE. BEST TO USE A NEW UNIQUE DATABASE NAME TO AVOID CONFLICT DIFFERENCES
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "USER": "admindjango", # 👈 AMEND DATABASE USER HERE
        "PASSWORD": "employee@123!", # 👈 AMEND DATABASE PASSWORD HERE
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'"  # handles invalid or missing values from being stored in the database by INSERT and UPDATE statements
        },
    }
}
```

**Note**: if you want to create new credentials based on the example default values, then run the following SQL commands individually, from within the MySQL shell:

```sql
CREATE USER 'admindjango'@'localhost' IDENTIFIED BY 'employee@123!';
GRANT ALL PRIVILEGES ON littlelemon_sayvai.* TO 'admindjango'@'localhost';
FLUSH PRIVILEGES;
```

**Note**: Also ensure your MySQL server is currently running on port 3306 (default). If not, then change the port number in the `settings.py` file.

ℹ️ - This step only needs to be done once, when you first install the app.

6. Run the individual migration commands in your terminal to create the necessary database tables in the MySQL database (littlelemon):

```shell
python3 manage.py makemigrations
python3 manage.py migrate
```

ℹ️ - This step only needs to be done once, when you first install the app.

7. Run the following command to start the Django development server:

```shell
python3 manage.py runserver
```

8. Create a super user admin account for the app via the terminal (e.g. username: `admin`, password: `admin` email: `admin@littlelemon.com`):

```shell
python3 manage.py createsuperuser
```

## Testing the app

The majority of the testing the listing of menu items derived from the database, and especially performing CRUD operations on table bookings, which can be done on [http://127.0.0.1:8000/restaurant/](http://127.0.0.1:8000/restaurant/).

1. Create a new group labelled as `Managers`, and assign the `admin` user to that group from within the [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) interface.

2. Register a new customer user account from [http://127.0.0.1:8000/restaurant/register](http://127.0.0.1:8000/restaurant/register), and then login at [http://127.0.0.1:8000/restaurant/login](http://127.0.0.1:8000/restaurant/login).

## Admin Credentials

To login to the localhost [admin](http://127.0.0.1:8000/admin) web UI interface of the app as the super user admin, use the following credentials:

```
username: admin
password: admin
```

The registered email address for the super user admin is `admin@littlelemon.com`.
