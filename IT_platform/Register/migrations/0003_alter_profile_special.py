# Generated by Django 5.1.3 on 2024-11-16 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0006_special_alter_event_special'),
        ('Register', '0002_alter_profile_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='special',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.PROTECT, to='Events.special'),
        ),
    ]