# Generated by Django 2.2.6 on 2021-09-08 17:48

import apps.data_entry.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_entry', '0003_position_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='hash_val',
            field=models.CharField(default=apps.data_entry.models.hash_val, max_length=64),
        ),
    ]
