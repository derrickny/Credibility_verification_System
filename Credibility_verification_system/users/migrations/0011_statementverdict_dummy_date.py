# Generated by Django 4.2.6 on 2023-11-17 04:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_statementverdict'),
    ]

    operations = [
        migrations.AddField(
            model_name='statementverdict',
            name='dummy_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
