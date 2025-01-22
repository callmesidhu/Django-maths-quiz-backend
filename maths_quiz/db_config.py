# db_config.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Use the MySQL backend
        'NAME': 'maths_app_db',         # Replace with your database name
        'USER': 'MySQLDB',         # Replace with your database username
        'PASSWORD': '12345678', # Replace with your database password
        'HOST': 'localhost',                  # Set to your MySQL host, e.g., '127.0.0.1'
        'PORT': '3306',                       # Default MySQL port
    }
}
