# Generated by Django 4.2.7 on 2023-11-30 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0014_remove_exerciseplan_movements_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyplan',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]