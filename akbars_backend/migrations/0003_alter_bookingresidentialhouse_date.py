# Generated by Django 4.0.4 on 2022-04-17 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akbars_backend', '0002_alter_bookingworkingroom_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingresidentialhouse',
            name='date',
            field=models.DateField(verbose_name='Дата заезда'),
        ),
    ]
