# Generated by Django 3.1.2 on 2021-11-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_no',
            field=models.IntegerField(unique=True),
        ),
    ]
