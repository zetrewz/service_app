# Generated by Django 4.0 on 2024-01-11 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_subscription_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='comment',
            field=models.CharField(db_index=True, default='', max_length=50),
        ),
    ]