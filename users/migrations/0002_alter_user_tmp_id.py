# Generated by Django 5.1.1 on 2024-10-29 18:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tmp_id',
            field=models.UUIDField(default=uuid.UUID('7e6b0d2d-f328-495f-85e1-7808d63a69df')),
        ),
    ]