# Generated by Django 5.1.1 on 2024-09-25 15:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profiles', '0005_alter_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2024, 9, 25, 17, 27, 17, 139956)),
        ),
    ]
