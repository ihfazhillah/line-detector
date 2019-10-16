# Generated by Django 2.2.6 on 2019-10-16 22:35

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='lines/')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('options', django.contrib.postgres.fields.jsonb.JSONField()),
                ('scale', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
