# Generated by Django 4.0.1 on 2022-07-07 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='grandTotal',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='number_of_products',
            field=models.IntegerField(default=1),
        ),
    ]
