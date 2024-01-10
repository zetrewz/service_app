from django.core.validators import MaxValueValidator
from django.db.models import Model, CharField, PositiveIntegerField, ForeignKey, PROTECT

from clients.models import Client
from services.tasks import set_price, set_comment


class Service(Model):
    name = CharField(max_length=50)
    full_price = PositiveIntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__full_price = self.full_price

    def save(self, *args, **kwargs):
        if self.full_price != self.__full_price:
            for subscription in self.subscriptions.all():
                set_price.delay(subscription.id)
                set_comment.delay(subscription.id)

        return super().save()


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__discount_percent = self.discount_percent

    def save(self, *args, **kwargs):
        if self.discount_percent != self.__discount_percent:
            for subscription in self.subscriptions.all():
                set_price.delay(subscription.id)
                set_comment.delay(subscription.id)

        return super().save()


class Subscription(Model):
    client = ForeignKey(Client, related_name='subscriptions', on_delete=PROTECT)
    service = ForeignKey(Service, related_name='subscriptions', on_delete=PROTECT)
    plan = ForeignKey(Plan, related_name='subscriptions', on_delete=PROTECT)
    price = PositiveIntegerField(default=0)
    comment = CharField(max_length=50, default='')
