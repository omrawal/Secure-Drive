# Generated by Django 3.1.6 on 2021-02-13 17:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('uid', models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_data', models.FileField(upload_to='uploads/')),
                ('fid', models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
