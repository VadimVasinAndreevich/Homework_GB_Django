from django.contrib import admin
from .models import Client, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_count(modeladmin, request, queryset):
    queryset.update(count=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['title', 'count', 'price']
    list_filter = ['date_add']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_count]

    """Отдельный продукт."""
    readonly_fields = ['date_add', 'count']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'подробное описание товара',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'count'],
            }
        ),
        (
            'дата',
            {
                'description': 'дата добавления продукта',
                'fields': ['date_add'],
            }
        ),
    ]


class ClientAdmin(admin.ModelAdmin):
    """Список клиентов."""
    list_display = ['name', 'email', 'telephone_number']
    list_filter = ['date_register', 'email', 'telephone_number']
    search_fields = ['name', 'email', 'telephone_number']
    search_help_text_name = 'Поиск по полю имя (name)'
    search_help_text_email = 'Поиск по полю email (email)'
    search_help_text_telephone_number = 'Поиск по полю номер телефона (telephone_number)'

    """Отдельный клиент."""
    readonly_fields = ['address', 'date_register']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Персональные данные',
            {
                'classes': ['collapse'],
                'description': 'персональные данные клиента',
                'fields': ['email', 'telephone_number', 'address'],
            },
        ),
        (
            'Дата регистрации',
            {
                'description': 'дата регистрации клиента',
                'fields': ['date_register'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    """Список заказов."""
    list_display = ['customer', 'total_price', 'date_order']
    list_filter = ['date_order']
    search_fields = ['total_price', 'date_order']
    search_help_text_total = 'Поиск по полю итоговая цена (total_price)'
    search_help_text_date = 'Поиск по полю дата заказа (date_order)'

    """Отдельный заказ."""
    readonly_fields = ['products']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer'],
            },
        ),
        (
            'Детали заказа',
            {
                'classes': ['collapse'],
                'description': 'детали заказа',
                'fields': ['products'],
            },
        ),
        (
            'Дата заказза',
            {
                'description': 'дата формирования заказа',
                'fields': ['date_order'],
            }
        ),
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
