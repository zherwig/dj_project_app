# Generated by Django 3.1 on 2021-04-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_completed_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='excludeFromReports',
            field=models.BooleanField(default=False),
        ),
    ]
