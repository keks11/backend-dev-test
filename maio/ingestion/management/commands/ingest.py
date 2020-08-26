import json
import redis
import time

from django.core.management.base import BaseCommand, CommandError
from ingestion import ingest


class Command(BaseCommand):
    help = 'Run the super duper awesome ingestion pipeline'

    def handle(self, *args, **options):
        ingest.run()
        self.stdout.write(self.style.SUCCESS('Ingestion pipeline ran: OK'))