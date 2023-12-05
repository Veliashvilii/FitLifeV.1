# Generated by Django 4.2.7 on 2023-12-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_remove_dailyplanfood_breakfast_foods_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseplan',
            name='friday',
            field=models.ManyToManyField(blank=True, null=True, related_name='friday_exercise', to='users.movement'),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='monday',
            field=models.ManyToManyField(blank=True, null=True, related_name='monday_exercise', to='users.movement'),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='saturday',
            field=models.ManyToManyField(blank=True, null=True, related_name='saturday_exercise', to='users.movement'),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='sunday',
            field=models.ManyToManyField(blank=True, null=True, related_name='sunday_exercise', to='users.movement'),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='thursday',
            field=models.ManyToManyField(blank=True, null=True, related_name='thursday_exercise', to='users.movement'),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='tuesday',
            field=models.ManyToManyField(blank=True, null=True, related_name='tuesday_exercise', to='users.movement'),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='wednesday',
            field=models.ManyToManyField(blank=True, null=True, related_name='wednesday_exercise', to='users.movement'),
        ),
        migrations.AlterField(
            model_name='foodplan',
            name='monday',
            field=models.ManyToManyField(blank=True, null=True, related_name='monday_food', to='users.food'),
        ),
        migrations.AlterField(
            model_name='foodplan',
            name='saturday',
            field=models.ManyToManyField(blank=True, null=True, related_name='saturday_food', to='users.food'),
        ),
        migrations.AlterField(
            model_name='foodplan',
            name='sunday',
            field=models.ManyToManyField(blank=True, null=True, related_name='sunday_food', to='users.food'),
        ),
        migrations.AlterField(
            model_name='foodplan',
            name='thursday',
            field=models.ManyToManyField(blank=True, null=True, related_name='thursday_food', to='users.food'),
        ),
        migrations.AlterField(
            model_name='foodplan',
            name='tuesday',
            field=models.ManyToManyField(blank=True, null=True, related_name='tuesday_food', to='users.food'),
        ),
        migrations.AlterField(
            model_name='foodplan',
            name='wednesday',
            field=models.ManyToManyField(blank=True, null=True, related_name='wednesday_food', to='users.food'),
        ),
    ]
