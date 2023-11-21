from django.core.management.base import BaseCommand
from myapp2.models import Client
from random import choice as ch, randint as ri
import datetime


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        streets = ['green', 'purple', 'republic', 'garden', 'friendly', 'lenin st.']
        for i in range(1, 21):
            month_30 = [4, 6, 9, 11]
            number = (f'+7({ri(0, 9)}{ri(0, 9)}{ri(0, 9)}){ri(0, 9)}{ri(0, 9)}'
                      f'{ri(0, 9)}-{ri(0, 9)}{ri(0, 9)}-{ri(0, 9)}{ri(0, 9)}')
            year = ri(2020, 2023)
            month = ri(1, 12)
            if month == 2:
                day = ri(1, 28)
            elif month in month_30:
                day = ri(1, 30)
            else:
                day = ri(1, 31)
            client = Client(name=f'client{i}',
                            email=f'client{i}@example.com',
                            telephone_number=number,
                            address=f'street {ch(streets)}, home {ri(1, 100)}',
                            date_register=datetime.date(year, month, day))
            client.save()
            self.stdout.write(f'{client}')
