This repository contains the source code for an Online Bakery System developed with Django. The system provides a web platform for managing bakery operations online, including inventory management, order processing, and user authentication. It utilizes Django for backend development and Django Rest Framework for creating RESTful APIs.

**Getting Started**

To get started with the Bakery API, you'll need to set up your development environment.

**Prerequisites**

- Python (3.8 or higher recommended)
- Django (3.2 or higher)
- Django REST Framework
- djangorestframework-simplejwt

**Installation**

First, clone the repository and install the required dependencies:

```bash
pip install django djangorestframework djangorestframework-simplejwt
```

After installing Django and Django REST Framework, you can proceed to set up your project and application.

**Setting up the Database**

You can use SQLite (default). Ensure your database settings in `settings.py` are correctly configured.
You can even use MYSQL, PostgresSQL

Run migrations to set up your database schema:

```bash
python manage.py makemigrations
python manage.py migrate
```

Running the Server:

Start the Django development server:

```bash
python manage.py runserver
```
