# Generated by Django 4.1.3 on 2022-11-13 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('member_age', models.IntegerField()),
                ('member_city', models.CharField(max_length=1024)),
                ('member_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Specialist',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('specialist_specialization', models.CharField(max_length=1024)),
                ('specialist_city', models.CharField(max_length=512)),
                ('specialist_phone', models.IntegerField()),
                ('specialist_specialization_image', models.ImageField(upload_to='images/')),
                ('specialist_image', models.ImageField(upload_to='images/')),
                ('specialist_personal_page', models.URLField()),
                ('specialist_rate', models.FloatField()),
                ('specialist_confirmation', models.BooleanField()),
            ],
        ),
    ]
