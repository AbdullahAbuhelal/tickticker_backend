# Generated by Django 5.1.1 on 2024-11-03 19:22

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_user_tmp_id_alter_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2cda13c3-ca2c-4865-b616-054d7d5c51dc'), editable=False, primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
