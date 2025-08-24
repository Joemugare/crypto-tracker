from django.core.management.base import BaseCommand
from tracker.utils import fetch_market_data

class Command(BaseCommand):
    help = 'Pre-caches market data to reduce API calls on startup'

    def handle(self, *args, **options):
        self.stdout.write("Pre-caching market data...")
        data = fetch_market_data()
        if data:
            self.stdout.write(self.style.SUCCESS(f"Successfully cached {len(data)} coins"))
        else:
            self.stdout.write(self.style.ERROR("Failed to cache market data"))