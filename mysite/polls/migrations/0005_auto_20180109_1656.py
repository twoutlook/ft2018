# Generated by Django 2.0.1 on 2018-01-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180109_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yazhu',
            name='work_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]