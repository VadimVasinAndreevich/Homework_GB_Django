from django.core.management.base import BaseCommand
from myapp2.models import Order, Client, Product
from random import choice as ch, randint as ri, uniform as ui
import datetime


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        for i in range(1, 21):
            customer = Client.objects.filter(pk=i).first()
            client_data = customer.date_register
            test_data = None
            x = ri(1, 20)
            y = 0
            product_id = []
            total_price = 0
            while y <= x:
                product = Product.objects.filter(pk=ri(1, 200)).first()
                product_data = product.date_add
                month_30 = [4, 6, 9, 11]
                year = ri(2020, 2023)
                month = ri(1, 12)
                if month == 2:
                    day = ri(1, 28)
                elif month in month_30:
                    day = ri(1, 30)
                else:
                    day = ri(1, 31)
                test_data = datetime.date(year, month, day)
                if product_data < test_data > client_data and product.count > 0:
                    product_id.append(product.id)
                    total_price += product.price
                    product.count -= 1
                    y += 1
                    #product.save()
            order = Order(customer=customer,
                          total_price=round(total_price, 2),
                          date_order=test_data)
            order.save()
            for el in product_id:
                order.products.add(Product.objects.filter(pk=el).first())
            self.stdout.write(f'{order}')
