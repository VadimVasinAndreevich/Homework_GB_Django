from django import forms
import datetime


class ClientForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    telephone_number = forms.CharField(max_length=100)
    address = forms.CharField(max_length=200)
    date_register = forms.DateField(initial=datetime.date.today,
                                    widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    def __str__(self):
        return (f'client: {self.name}, email: {self.email}, telephone_number:{self.telephone_number},'
                f'address:{self.address}, date_register:{self.date_register}')


class ProductForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField()
    price = forms.FloatField()
    count = forms.IntegerField()
    date_add = forms.DateField(initial=datetime.date.today,
                               widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))

    def __str__(self):
        return (f'product: {self.title}, description: {self.description}, price:{self.price},'
                f'count:{self.count}, date_add:{self.date_add}')