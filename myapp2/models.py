from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    date_register = models.DateField(auto_now_add=False)

    def __str__(self):
        return (f'client: {self.name}, email: {self.email}, telephone_number:{self.telephone_number},'
                f'address:{self.address}, date_register:{self.date_register}')


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    price = models.FloatField()
    count = models.IntegerField()
    date_add = models.DateField(auto_now_add=False)

    def __str__(self):
        return (f'product: {self.title}, description: {self.description}, price:{self.price},'
                f'count:{self.count}, date_add:{self.date_add}')


class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.FloatField()
    date_order = models.DateField(auto_now_add=False)

    def __str__(self):
        return (f'customer: {self.customer}, products: {self.products}, total_price:{self.total_price},'
                f'date_order:{self.date_order}')
