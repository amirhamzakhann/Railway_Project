# Generated by Django 3.2.7 on 2021-09-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('railapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='railschedule',
            name='journey_date',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='Date',
        ),
    ]
