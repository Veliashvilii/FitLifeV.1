# Generated by Django 4.2.7 on 2023-12-04 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_alter_exerciseplan_friday_alter_exerciseplan_monday_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercurrent',
            name='user',
        ),
        migrations.AddField(
            model_name='userextra',
            name='current_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.usercurrent'),
        ),
    ]
