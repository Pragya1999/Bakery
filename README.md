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

**API Endpoints**

Admin Endpoints:

Admin endpoints require admin privileges. These endpoints allow managing ingredients and bakery items.

- **Add Ingredients**: `POST /api/ingredients/`
- **Create Bakery Item**: `POST /api/bakery-items/`
- **Get Bakery Item Details**: `GET /api/bakery-items/{id}/`
- **Manage Inventory**: Direct interaction with ingredient model.

Customer Endpoints:

Customer endpoints are designed for end-users to interact with the bakery.

- **User Registration**: `POST /api/register/`
 
  Allows new users to register. Users need to provide a username, password, and email.

- **User Authentication**: `POST /api/token/`
 
  Authenticates a user and returns a JWT token.

- **List and Search Products**: `GET /api/products/`
 
  Returns a list of available bakery items. Supports search functionality via the `search` query parameter.

- **Place an Order**: `POST /api/order/`
 
  Enables customers to place an order, specifying the items and quantities.

- **View Order History**: `GET /api/order/history/`

  Allows customers to view their past orders and details.


  **Models**

The application uses several models to represent users, bakery items, ingredients, and orders.

- `User`: Extended Django User model with admin and customer flags.
- `Ingredient`: Represents an ingredient used in bakery items.
- `BakeryItem`: Represents a product available for purchase.
- `BakeryItemIngredient`: Intermediary model linking bakery items and ingredients with quantity percentage.
- `Order`: Represents a customer's order.
- `OrderItem`: Represents an item within an order, linking to `BakeryItem`.

**Serializers**

Serializers convert complex data types to Python data types that can then be easily rendered into JSON. The API uses serializers for user registration, JWT token handling, bakery items, and orders.

**Permissions**

The API differentiates between admin and customer users, providing different permissions and access levels for each user type.

- Admin users have full access to all admin endpoints.
- Customer users can access endpoints related to placing orders, viewing products, and checking their order history.


**Security**

- Authentication is managed using JSON Web Tokens (JWT), ensuring secure access to the API.
- Passwords are hashed using Django's built-in password hashing mechanisms.
