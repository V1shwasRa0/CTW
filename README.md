Project Structure

*Main things are commented

CTW/
|
|-- CTW/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|
|-- myApp/                          # Work under this folder
|   |-- migrations/
|   |-- templates/                  # Place your html files here
|       |-- ourImpact.html
|       |-- home.html
|       |-- aboutus.html
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py                     # Define urls
|   |-- views.py                    # Define views
|
|-- manage.py