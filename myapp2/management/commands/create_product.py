from django.core.management.base import BaseCommand
from myapp2.models import Product
from random import choice as ch, randint as ri, uniform as ui
import datetime


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('start', type=int, help='start_number_range')
        parser.add_argument('end', type=int, help='end_number_range')

    def handle(self, *args, **kwargs):
        start = kwargs.get('start')
        end = kwargs.get('end')
        for i in range(start, end+1):
            month_30 = [4, 6, 9, 11]
            year = ri(2020, 2023)
            month = ri(1, 12)
            if month == 2:
                day = ri(1, 28)
            elif month in month_30:
                day = ri(1, 30)
            else:
                day = ri(1, 31)
            product = Product(title=f'product{i}',
                              description=f'this is product {i}',
                              price=round(ui(0.01, 100.01), 2),
                              count=100,
                              date_add=datetime.date(year, month, day))
            product.save()
            self.stdout.write(f'{product}')
