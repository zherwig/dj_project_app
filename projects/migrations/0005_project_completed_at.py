# Generated by Django 3.1 on 2020-09-25 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
