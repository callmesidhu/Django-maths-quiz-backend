from django.apps import AppConfig # type: ignore
from django.db.backends.signals import connection_created # type: ignore
import logging

logger = logging.getLogger(__name__)

class YourAppNameConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maths_app'

    def ready(self):
        # Connect the signal to a custom handler
        connection_created.connect(log_db_connection)

def log_db_connection(sender, **kwargs):
    logger.info("Database connection established successfully.")
    print("Database connection established successfully.")
