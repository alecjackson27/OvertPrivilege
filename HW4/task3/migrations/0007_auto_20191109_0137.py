# Generated by Django 2.2.6 on 2019-11-09 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task3', '0006_user_salt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='zip',
            field=models.CharField(max_length=5),
        ),
    ]
