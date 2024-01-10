from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField

from services.models import Subscription, Plan


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class SubscriptionSerializer(ModelSerializer):
    plan = PlanSerializer()
    client_name = CharField(source='client.company_name')
    email = CharField(source='client.user.email')
    # price = SerializerMethodField()
    #
    # def get_price(self, instance):
    #     return instance.price

    class Meta:
        model = Subscription
        fields = ('id', 'plan_id', 'client_name', 'email', 'plan', 'price')
