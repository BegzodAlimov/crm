from django.db import models
from django.db.models import CharField

from tools.models import BasedModel
from users.models import Student, Teacher


class Room(BasedModel):
    room_number = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.room_number}'


class Subject(BasedModel):
    subject_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.subject_name


class Level(BasedModel):
    level_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.level_name


class Course(BasedModel):
    DAY_CHOICES = [
        ('every_day', 'Every day'),
        ('odd_day', 'Odd day'),
        ('even_day', 'Even day')
    ]
    course_name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='my_groups')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_groups')
    price = models.IntegerField()
    period = CharField(max_length=50)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='level_groups')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room_groups')
    students = models.ManyToManyField(Student, related_name='student_groups')
    day = models.CharField(max_length=50, choices=DAY_CHOICES)
    begin_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.course_name} {self.level} - {self.teacher} {self.begin_time} - {self.end_time}'
