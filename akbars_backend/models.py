from django.db import models
from django.contrib.auth.models import User


class ResidentialHouse(models.Model):
    name_of_house = models.CharField('Название дома', max_length=50)
    count_of_beds = models.PositiveSmallIntegerField('Количестве спальных мест', default=1)
    square = models.PositiveSmallIntegerField('Площадь комнаты, м2', default=10)
    cost = models.PositiveSmallIntegerField('Стоимость проживания, руб/сут', default=1000)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return f'{self.name_of_house} ({self.count_of_beds}-местный)'

    class Meta:
        verbose_name = 'Жилой дом'
        verbose_name_plural = 'Жилые дома'


class BookingResidentialHouse(models.Model):
    user = models.ForeignKey(User, verbose_name='Гость', on_delete=models.CASCADE)
    residential_house = models.ForeignKey(ResidentialHouse, verbose_name='Дом', on_delete=models.CASCADE)
    count_of_day = models.PositiveSmallIntegerField('Количество ночей', default=1)
    date = models.DateField('Дата заезда')
    participants = models.TextField('Участники', blank=True)

    def __str__(self):
        return f'Бронь. Гость: {self.user.username}, Дата: {self.date}'

    class Meta:
        verbose_name = 'Бронирование дома'
        verbose_name_plural = 'Бронирования домов'


class WorkingRoom(models.Model):
    VAR = (('Коворкинг', 'Коворкинг'),
           ('Актовый зал', 'Актовый зал'),
           ('Спортивный зал', 'Спортивный зал'))

    type = models.CharField('Тип комнаты', choices=VAR, max_length=20)
    name_of_room = models.CharField('Номер комнаты', max_length=20)
    count_of_seats = models.PositiveSmallIntegerField('Количество мест', default=1)
    description = models.TextField('Описание')

    def __str__(self):
        return f'{self.type} {self.name_of_room}'

    class Meta:
        verbose_name = 'Помещение для бронирования'
        verbose_name_plural = 'Помещения для бронирования'


class BookingWorkingRoom(models.Model):
    user = models.ForeignKey(User, verbose_name='Гость', on_delete=models.CASCADE)
    working_room = models.ForeignKey(WorkingRoom, verbose_name='Помещение', on_delete=models.CASCADE)
    datetime = models.DateTimeField('Дата и время бронирования')
    theme_of_events = models.CharField('Тема мероприятия', max_length=100)
    participants = models.TextField('Участники', blank=True)

    def __str__(self):
        return f'Гость: {self.user.username}, комната: {self.working_room.type} {self.working_room.name_of_room}, Дата: {self.datetime}'

    class Meta:
        verbose_name = 'Бронирование помещения'
        verbose_name_plural = 'Бронирования помещений'

