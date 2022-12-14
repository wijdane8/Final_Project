# Generated by Django 4.1.3 on 2022-11-14 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='member_name',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialist',
            name='specialist_name',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='member_age',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_city',
            field=models.CharField(default='', max_length=1024),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_image',
            field=models.ImageField(default='/media/images/OIP.jpeg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialist_city',
            field=models.CharField(default='', max_length=512),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialist_confirmation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialist_image',
            field=models.ImageField(default='/media/images/OIP.jpeg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialist_personal_page',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialist_phone',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialist_rate',
            field=models.FloatField(default=5),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialist_specialization',
            field=models.CharField(default='psycologist', max_length=1024),
        ),
        migrations.AlterField(
            model_name='specialist',
            name='specialist_specialization_image',
            field=models.ImageField(default='/media/images/OIP.jpeg', upload_to='pdfs/'),
        ),
    ]
