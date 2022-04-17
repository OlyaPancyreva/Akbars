# Generated by Django 4.0.4 on 2022-04-17 10:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ResidentialHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_house', models.CharField(max_length=50, verbose_name='Название дома')),
                ('count_of_beds', models.PositiveSmallIntegerField(default=1, verbose_name='Количестве спальных мест')),
                ('square', models.PositiveSmallIntegerField(default=10, verbose_name='Площадь комнаты, м2')),
                ('cost', models.PositiveSmallIntegerField(default=1000, verbose_name='Стоимость проживания, руб/сут')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Жилой дом',
                'verbose_name_plural': 'Жилые дома',
            },
        ),
        migrations.CreateModel(
            name='WorkingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Коворкинг', 'Коворкинг'), ('Актовый зал', 'Актовый зал'), ('Спортивный зал', 'Спортивный зал')], max_length=20, verbose_name='Тип комнаты')),
                ('name_of_room', models.CharField(max_length=20, verbose_name='Номер комнаты')),
                ('count_of_seats', models.PositiveSmallIntegerField(default=1, verbose_name='Количество мест')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Помещение для бронирования',
                'verbose_name_plural': 'Помещения для бронирования',
            },
        ),
        migrations.CreateModel(
            name='BookingWorkingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='Дата и время бронирования')),
                ('theme_of_events', models.CharField(max_length=100, verbose_name='Тема мероприятия')),
                ('participants', models.TextField(verbose_name='Участники')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Гость')),
                ('working_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akbars_backend.workingroom', verbose_name='Помещение')),
            ],
            options={
                'verbose_name': 'Бронирование помещения',
                'verbose_name_plural': 'Бронирования помещений',
            },
        ),
        migrations.CreateModel(
            name='BookingResidentialHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_of_day', models.PositiveSmallIntegerField(default=1, verbose_name='Количество ночей')),
                ('date', models.DateTimeField(verbose_name='Дата заезда')),
                ('participants', models.TextField(verbose_name='Участники')),
                ('residential_house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akbars_backend.residentialhouse', verbose_name='Дом')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Гость')),
            ],
            options={
                'verbose_name': 'Бронирование дома',
                'verbose_name_plural': 'Бронирования домов',
            },
        ),
    ]
