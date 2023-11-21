from django.views import View
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Product, Client, Order
from .forms import ClientForm, ProductForm
from django.http import HttpResponse
import logging
import datetime

logger = logging.getLogger(__name__)


def links(request):
    logger.info(f'Transition on links, {datetime.datetime.now()}')
    return render(request, "myapp2/index.html")


def product_reader(request):
    logger.info(f'Transition on products, {datetime.datetime.now()}')
    return HttpResponse(Product.objects.all())


def client_reader(request):
    logger.info(f'Transition on list_clients, {datetime.datetime.now()}')
    return HttpResponse(Client.objects.all())


def order_reader(request):
    logger.info(f'Transition on orders, {datetime.datetime.now()}')
    return HttpResponse(Order.objects.all())


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            telephone_number = form.cleaned_data['telephone_number']
            address = form.cleaned_data['address']
            date_register = form.cleaned_data['date_register']
            logger.info(f'Получили {name=}, {email=}, {telephone_number=}, {address=}, {date_register=}.')
            client = Client(name=name, email=email,
                            telephone_number=telephone_number, address=address, date_register=date_register)
            client.save()
            message = 'Пользователь сохранён'
    else:
        form = ClientForm()
        message = 'Заполните форму'
    return render(request, 'myapp2/add_form.html', {'form': form, 'message': message})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            date_add = form.cleaned_data['date_add']
            logger.info(f'Получили {title=}, {description=}, {image=}, {price=}, {count=}, {date_add=}.')
            product = Product(title=title, description=description, image=image,
                              price=price, count=count, date_add=date_add)
            product.save()
            message = 'Продукт внесён'
    else:
        form = ProductForm()
        message = 'Заполните форму'
    return render(request, 'myapp2/add_form.html', {'form': form, 'message': message})