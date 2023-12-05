# Generated by Django 4.2.7 on 2023-12-05 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_userextra_food_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodplan',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='foodplan',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='foodplan',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='foodplan',
            name='sunday',
        ),
        migrations.RemoveField(
            model_name='foodplan',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='foodplan',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='foodplan',
            name='wednesday',
        ),
        migrations.AddField(
            model_name='foodplan',
            name='friday_breakfast',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_food_breakfast', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='friday_dinner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_food_dinner', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='friday_lunch',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_food_lunch', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='friday_snacks',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friday_food_snacks', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='monday_breakfast',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_food_breakfast', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='monday_dinner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_food_dinner', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='monday_lunch',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_food_lunch', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='monday_snacks',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monday_food_snacks', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='saturday_breakfast',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_food_breakfast', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='saturday_dinner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_food_dinner', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='saturday_lunch',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_food_lunch', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='saturday_snacks',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saturday_food_snacks', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='sunday_breakfast',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_food_breakfast', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='sunday_dinner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_food_dinner', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='sunday_lunch',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_food_lunch', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='sunday_snacks',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sunday_food_snacks', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='thursday_breakfast',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_food_breakfast', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='thursday_dinner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_food_dinner', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='thursday_lunch',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_food_lunch', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='thursday_snacks',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thursday_food_snacks', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='tuesday_breakfast',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_food_breakfast', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='tuesday_dinner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_food_dinner', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='tuesday_lunch',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_food_lunch', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='tuesday_snacks',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_food_snacks', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='wednesday_breakfast',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_food_breakfast', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='wednesday_dinner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_food_dinner', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='wednesday_lunch',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_food_lunch', to='users.food'),
        ),
        migrations.AddField(
            model_name='foodplan',
            name='wednesday_snacks',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_food_snacks', to='users.food'),
        ),
    ]