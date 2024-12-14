# Generated by Django 5.1.4 on 2024-12-12 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_gender_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10, null=True),
        ),
    ]
