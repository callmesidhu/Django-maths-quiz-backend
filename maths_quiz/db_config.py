from django.db.backends.signals import connection_created
from django.dispatch import receiver
import logging

# Configure logging for the database connection message
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'maths_app_db',        
        'USER': 'root',        
        'PASSWORD': '12345678', 
        'HOST': '127.0.0.1',                 
        'PORT': '3306',                       
    }
}

@receiver(connection_created)
def on_connection_created(sender, connection, **kwargs):
    if connection.vendor == 'mysql':
        logger.info("Database connected successfully!")
