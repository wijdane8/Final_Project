# Generated by Django 4.1.3 on 2022-11-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_member_member_name_specialist_specialist_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialist',
            name='specialist_information',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]