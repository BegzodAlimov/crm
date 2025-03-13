from django.db import models
from tools.models import BasedModel
from django.db.models import CharField
from users.models import User


class Room(BasedModel):
    room_number = models.CharField(unique=True, max_length=150)

    def __str__(self):
        return f'{self.room_number}'


class Level(BasedModel):
    level_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.level_name


class Subject(BasedModel):
    subject_name = models.CharField(max_length=50, unique=True)
    teacher = models.ManyToManyField(User, related_name='my_subjects', blank=True)

    def __str__(self):
        return self.subject_name


class Group(BasedModel):
    DAY_CHOICES = [
        ('every_day', 'Every day'),
        ('odd_day', 'Odd day'),
        ('even_day', 'Even day')
    ]

    group_name = models.CharField(max_length=120)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='my_groups')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_groups')
    price = models.IntegerField()
    period = CharField(max_length=50)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='level_groups')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_groups')
    students = models.ManyToManyField(User, related_name='student_groups', blank=True)
    day = models.CharField(max_length=50, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.group_name} {self.level} - {self.teacher} {self.start_time} - {self.end_time}'
