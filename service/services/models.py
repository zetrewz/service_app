from django.core.validators import MaxValueValidator
from django.db.models import Model, CharField, PositiveIntegerField, ForeignKey, PROTECT

from clients.models import Client


class Service(Model):
    name = CharField(max_length=50)
    full_price = PositiveIntegerField()


class Plan(Model):
    PLAN_TYPES = (
        ('full', 'Full'),
        ('student', 'Student'),
        ('discount', 'Discount')
    )

    plan_type = CharField(choices=PLAN_TYPES, max_length=10)
    discount_percent = PositiveIntegerField(default=0,
                                            validators=[
                                                MaxValueValidator
                                            ])


class Subscription(Model):
    client = ForeignKey(Client, related_name='subscriptions', on_delete=PROTECT)
    service = ForeignKey(Service, related_name='subscriptions', on_delete=PROTECT)
    plan = ForeignKey(Plan, related_name='subscriptions', on_delete=PROTECT)
