# Python Code
# myapp/management/commands/mytask.py

from django.core.management.base import BaseCommand, CommandError
from newsapp.views import baseScrape
class Command(BaseCommand):
    help = 'Type the help text here'

    def handle(self, *args, **options):
        # Add yout logic here
        # This is the task that will be run
        print("Ran BaseScrape()")
        baseScrape()