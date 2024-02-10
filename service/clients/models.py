from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, PROTECT, CharField


class Client(Model):
    user = OneToOneField(User, on_delete=PROTECT)
    company_name = CharField(max_length=100)
    full_address = CharField(max_length=100)
