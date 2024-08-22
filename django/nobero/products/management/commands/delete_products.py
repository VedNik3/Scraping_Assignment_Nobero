from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Delete all products'

    def handle(self, *args, **kwargs):
        # Count the number of products before deletion
        count = Product.objects.count()
        
        # Delete all products
        Product.objects.all().delete()
        
        # Output the number of deleted products
        self.stdout.write(self.style.SUCCESS(f'Deleted {count} products'))
