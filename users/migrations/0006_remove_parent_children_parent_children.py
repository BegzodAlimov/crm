# Generated by Django 5.1.4 on 2024-12-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_parent_children'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='children',
        ),
        migrations.AddField(
            model_name='parent',
            name='children',
            field=models.ManyToManyField(blank=True, null=True, related_name='children', to='users.student'),
        ),
    ]