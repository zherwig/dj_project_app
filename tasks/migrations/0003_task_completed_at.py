# Generated by Django 3.1 on 2020-09-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200904_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
