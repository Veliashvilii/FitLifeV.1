# Generated by Django 4.2.7 on 2023-12-03 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_alter_teacherextra_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyplanexercise',
            name='day',
            field=models.CharField(blank=True, choices=[('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday'), ('sunday', 'Sunday')], max_length=10),
        ),
    ]
