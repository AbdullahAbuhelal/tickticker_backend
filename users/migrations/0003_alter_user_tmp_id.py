# Generated by Django 5.1.1 on 2024-10-29 18:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_tmp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tmp_id',
            field=models.UUIDField(default=uuid.UUID('06d410c3-aef0-4cc0-ad79-7c71ed3b3406')),
        ),
    ]
