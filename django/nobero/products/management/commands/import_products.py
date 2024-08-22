import json
from django.core.management.base import BaseCommand
from products.models import Product
import os

class Command(BaseCommand):
    help = 'Load products data'

    def handle(self, *args, **kwargs):
        json_file_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
            'data', 
            'products.json'
        )

        with open(json_file_path, 'r') as f:
            data = json.load(f)
            for item in data:
                Product.objects.create(
                    category=item['category'],
                    url=item['url'],
                    title=item['title'],
                    last_7_day_sale=item['last_7_day_sale'],
                    available_skus=item['available_skus'],
                    fit=item['fit'],
                    fabric=item['fabric'],
                    neck=item['neck'],
                    sleeve=item['sleeve'],
                    pattern=item['pattern'],
                    length=item['length'],
                    description=item['description'],
                    image_url=item['image_url']
                )
