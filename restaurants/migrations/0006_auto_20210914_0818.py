# Generated by Django 3.2.7 on 2021-09-14 15:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_phonemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PhoneModel',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
