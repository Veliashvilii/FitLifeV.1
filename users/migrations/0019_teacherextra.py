# Generated by Django 4.2.7 on 2023-12-01 21:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0018_remove_dailyplanfood_foods_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('master_topic', models.CharField(blank=True, max_length=60, null=True)),
                ('experience', models.CharField(blank=True, max_length=140, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
