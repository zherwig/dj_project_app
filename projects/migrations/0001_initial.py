# Generated by Django 3.1 on 2020-08-28 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('detail', models.TextField(blank=True)),
                ('closed', models.BooleanField()),
                ('onHold', models.BooleanField()),
                ('priority', models.IntegerField()),
                ('placeInOrder', models.IntegerField()),
                ('duedate', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField()),
                ('assignee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_projects', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_projects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
