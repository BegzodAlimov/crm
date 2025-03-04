# Generated by Django 5.1.4 on 2025-03-01 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(related_name='student_groups', to='users.student'),
        ),
        migrations.AddField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_groups', to='users.teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level_groups', to='education.level'),
        ),
        migrations.AddField(
            model_name='group',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_groups', to='education.room'),
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ManyToManyField(related_name='subjects', to='users.teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_groups', to='education.subject'),
        ),
    ]
