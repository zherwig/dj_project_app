# Generated by Django 3.1 on 2020-08-29 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200828_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='detail',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='duedate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='placeInOrder',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]