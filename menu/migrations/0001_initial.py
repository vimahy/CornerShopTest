# Generated by Django 3.0.8 on 2021-03-30 17:44

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.TextField(max_length=50)),
                ('is_sent', models.BooleanField(default=False, help_text=())),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Date time on which the object was created.')),
            ],
            options={
                'ordering': ['-created_at'],
                'get_latest_by': 'created_at',
            },
        ),
    ]
