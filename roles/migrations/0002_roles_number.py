# Generated by Django 5.1.1 on 2024-09-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roles',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
