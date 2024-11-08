# Generated by Django 5.1.1 on 2024-10-29 18:53

import uuid
from django.db import migrations, models

def copy_uuid_to_temp_id(apps, schema_editor):
    User = apps.get_model('users', 'User')
    for user in User.objects.all():

        if not user.tmp_id:
            user.tmp_id = uuid.uuid4()
            user.save()

        user.id = user.tmp_id
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_username_alter_user_id_alter_user_tmp_id'),
    ]

    operations = [

        # migrations.RunPython(copy_uuid_to_temp_id)
    ]
