# Generated by Django 4.2.7 on 2023-12-02 20:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0022_teacherextra_students_alter_userextra_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextra',
            name='trainer',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_user': 0}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_trainer', to=settings.AUTH_USER_MODEL),
        ),
    ]
