"""
Django command to wait for the database to be available
"""

import time

# from psycopg2 import OperationalError as Psycopg2OpError

# from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Wait for the database to be available"""

    def handle(self, *args, **options):

        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except Exception as err:
                print()
                self.stdout.write(
                    f"Database unavailable, waiting for 1 second, Error: {err}"
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
