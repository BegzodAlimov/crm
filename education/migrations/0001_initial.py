# Generated by Django 5.1.4 on 2024-12-14 12:00

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_alter_user_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('level_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room_number', models.IntegerField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject_name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('period', models.CharField(max_length=50)),
                ('day', models.CharField(choices=[('every_day', 'Every day'), ('odd_day', 'Odd day'), ('even_day', 'Even day')], max_length=50)),
                ('begin_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('students', models.ManyToManyField(related_name='student_groups', to='users.student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_groups', to='users.teacher')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level_groups', to='education.level')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_groups', to='education.room')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_groups', to='education.subject')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
