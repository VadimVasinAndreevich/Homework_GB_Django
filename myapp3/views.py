from django.views import View
from django.shortcuts import render
from myapp2.models import Client, Product, Order
import datetime


def index(request):
    start_data_365 = datetime.date(2022, 12, 31)
    start_data_30 = datetime.date(2023, 12, 1)
    start_data_7 = datetime.date(2023, 12, 24)
    end_data = datetime.date(2023, 12, 31)
    data_list = [start_data_365, start_data_30, start_data_7]
    my_dict = {}
    for data in data_list:
        for i in range(1, 21):
            orders = Order.objects.filter(customer_id=i).all()
            customer_id_list = [order.pk for order in orders if data <= order.date_order <= end_data]
            all_prod_set = set([])
            for el in customer_id_list:
                test = Order.objects.get(pk=el)
                prod = test.products.all()
                prod_list = [elem.title for elem in prod]
                for element in prod_list:
                    all_prod_set.add(element)
            all_prod_list = list(all_prod_set)
            if len(all_prod_list) == 0:
                my_dict[f'list prod ({data} - {end_data}), client{i}'] = "orders no"
            else:
                my_dict[f'list prod ({data} - {end_data}), client{i}'] = all_prod_list
    context = {'my_dict': my_dict}
    return render(request, 'myapp3/index.html', context)
