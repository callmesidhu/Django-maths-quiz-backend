from decouple import config # type: ignore
from django.db.backends.signals import connection_created  # type: ignore
from django.dispatch import receiver  # type: ignore
import logging

# Configure logging for the database connection message
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'), 
        'NAME': config('DB_NAME'),        
        'USER': config('DB_USER'),        
        'PASSWORD': config('DB_PASSWORD'), 
        'HOST': config('DB_HOST'),                  
        'PORT': config('DB_PORT'),                    
    }
}

@receiver(connection_created)
def on_connection_created(sender, connection, **kwargs):
    if connection.vendor == 'mysql':
        logger.info("Database connected successfully!")
