# Generated by Django 4.1.3 on 2022-11-15 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_member_type_specialist_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='member_image',
        ),
    ]