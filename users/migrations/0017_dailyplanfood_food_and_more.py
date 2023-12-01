# Generated by Django 4.2.7 on 2023-12-01 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0016_remove_dailyplan_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPlanFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='DailyPlan',
            new_name='DailyPlanExercise',
        ),
        migrations.CreateModel(
            name='FoodPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.CharField(blank=True, max_length=140, null=True)),
                ('cal_goal', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('daily_plans', models.ManyToManyField(blank=True, to='users.dailyplanfood')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='dailyplanfood',
            name='foods',
            field=models.ManyToManyField(blank=True, to='users.food'),
        ),
    ]
