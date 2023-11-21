from django.core.management.base import BaseCommand
from myapp2.models import Client, Product, Order
import datetime


class Command(BaseCommand):
    help = "Get user by id."

    def handle(self, *args, **kwargs):
        start_data_365 = datetime.date(2022, 12, 31)
        start_data_30 = datetime.date(2023, 12, 1)
        start_data_7 = datetime.date(2023, 12, 24)
        end_data = datetime.date(2023, 12, 31)
        data_list = [start_data_365, start_data_30, start_data_7]
        for data in data_list:
            start_data = data
            for i in range(2, 3):
                orders = Order.objects.filter(customer_id=i).all()
                customer_id_list = [order.pk for order in orders if start_data <= order.date_order <= end_data]
                all_prod_set = set([])
                for el in customer_id_list:
                    test = Order.objects.get(pk=el)
                    prod = test.products.all()
                    prod_list = [elem.title for elem in prod]
                    for element in prod_list:
                        all_prod_set.add(element)
                all_prod_list = list(all_prod_set)
                print(all_prod_list)
