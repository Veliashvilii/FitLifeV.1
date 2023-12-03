# Generated by Django 4.2.7 on 2023-12-03 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_dailyplanexercise_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercisemovement',
            name='movement_type',
        ),
        migrations.AddField(
            model_name='exercisemovement',
            name='movement_type',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.movement'),
        ),
    ]
