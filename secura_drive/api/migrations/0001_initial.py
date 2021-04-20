# Generated by Django 3.1.6 on 2021-02-14 05:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_data', models.FileField(upload_to='uploads/')),
                ('fid', models.CharField(default=uuid.uuid4, max_length=200, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('modified_at', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
        ),
    ]