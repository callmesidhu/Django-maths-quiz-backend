# db_config.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'maths_app_db',        
        'USER': 'MySQLDB',        
        'PASSWORD': '12345678', 
        'HOST': 'localhost',                 
        'PORT': '3306',                       
    }
}
