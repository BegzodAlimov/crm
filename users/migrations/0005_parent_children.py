# Generated by Django 5.1.4 on 2024-12-20 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='children',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='users.student'),
        ),
    ]
