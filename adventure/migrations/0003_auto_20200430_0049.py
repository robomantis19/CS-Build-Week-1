# Generated by Django 3.0.5 on 2020-04-30 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0002_auto_20200429_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='e_to',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='n_to',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='s_to',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='room',
            name='w_to',
            field=models.IntegerField(default=0),
        ),
    ]