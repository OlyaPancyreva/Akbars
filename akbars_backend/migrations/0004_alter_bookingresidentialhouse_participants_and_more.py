# Generated by Django 4.0.4 on 2022-04-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akbars_backend', '0003_alter_bookingresidentialhouse_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingresidentialhouse',
            name='participants',
            field=models.TextField(blank=True, verbose_name='Участники'),
        ),
        migrations.AlterField(
            model_name='bookingworkingroom',
            name='participants',
            field=models.TextField(blank=True, verbose_name='Участники'),
        ),
    ]