# Generated by Django 5.1.3 on 2024-11-10 17:53

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('feedback', models.CharField(max_length=255, unique=True)),
                ('status', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'feedback',
                'ordering': ['-createdAt'],
            },
        ),
    ]
