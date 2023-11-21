from django.core.management.base import BaseCommand
from myapp2.models import Client, Product


class Command(BaseCommand):
    help = "multi-profile 1 - del client, 2 - del product,."

    def add_arguments(self, parser):
        parser.add_argument('command_number', type=int, help='number_signal')
        parser.add_argument('i', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        i = kwargs.get('i')
        if kwargs.get('command_number') == 1:
            client = True
            while client is not None:
                client = Client.objects.filter(pk=i).first()
                client.delete()
                self.stdout.write(f'{client}')
                i += 1
        elif kwargs.get('command_number') == 1:
            product = True
            while product is not None:
                product = Product.objects.filter(pk=i).first()
                product.delete()
                self.stdout.write(f'{product}')
                i += 1
