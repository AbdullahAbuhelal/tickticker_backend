# Generated by Django 5.1.1 on 2024-10-29 18:44

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_tmp_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tmp_id',
            field=models.UUIDField(default=uuid.UUID('51157fda-fb00-4265-a82a-31468a195909')),
        ),
    ]