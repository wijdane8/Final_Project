# Generated by Django 4.1.3 on 2022-11-16 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_specialist_type'),
        ('Website', '0004_group_group_info_group_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='member',
            field=models.ManyToManyField(to='accounts.member'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('Article', 'Article'), ('story', 'Story')], default='Article', max_length=64),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(),
        ),
    ]
