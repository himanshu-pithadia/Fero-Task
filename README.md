# Fero ecommerce backend task

#### Installation

1) clone repository in your local
2) install virtualenv with command "pip install virtualenv"
3) after installation of virtualenv create virtual environment run command "virtualenv venv".
4) after creating virtualenv activate it by comman for windows ".\venv\scripts\activate".
5) after activate virtualenv install requirments with command "pip install -r requirements.txt".

#### I dont use env file for configure database in settings.py so needs to add manually in setting.py file.

#### After configur database run command python manage.py migrate to apply migations.

#### After migrate run command python manage.py runserver to run the server.

## I added well structure code with filter options by using django-filter package

# After run the server you can test below API Endpoints

###### • Customers:
1) List all customers: GET /api/customers/
2) Create a new customer: POST /api/customers/
3) Update exiting customer: PUT /api/customers/<id>/
   
###### • Products:
1) List all products: GET /api/products/
2) Create a new product: POST /api/products/

###### • Orders:
1) List all orders: GET /api/orders/
2) Create a new order with multiple product and corresponding quantity: POST
/api/orders/
3) Edit existing order: PUT /api/orders/<id>/
4) List order based on the products: GET /api/orders/?products=Book,Pen
5) List order based on the customer: GET /api/orders/?customer=Sam

###### Validations (This must be in serializers)
1) Customer's and product’s name must be unique
2) Weight in positive decimal and not more than 25kg
3) Order cumulative weight must be under 150kg
4) Order Date cannot be in past.
   
###### Example Payload of Order Creation:
{
"customer": 2,
"order_date": "31/12/2023",
"address": "Test Address",
"order_item": [
{
"product": 1,
"quantity": 1,
},
{
"product": 7,
"quantity": 2,
},
{
"product": 4,
"quantity": 3,
}
]
}
