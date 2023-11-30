from django.db import models
from django.contrib.auth.models import User


class UserExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pics/", null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class UserCurrent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    weight_kg = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True
    )
    height_cm = models.PositiveIntegerField(null=True, blank=True)
    body_fat_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    muscle_mass_kg = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    bmi = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Movement(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    goal = models.CharField(max_length=140, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class ExerciseMovement(models.Model):
    movement_type = models.ManyToManyField(Movement, blank=True)
    set_value = models.IntegerField(blank=True, null=True)
    repeat_value = models.IntegerField(blank=True, null=True)

    def get_movement_name(self):
        if self.movement_type.exists():
            return self.movement_type.last().name
        else:
            return "No Movement Selected"

    def __str__(self):
        return f"{self.get_movement_name()}"


class DailyPlan(models.Model):
    DAY_CHOICES = [
        ("monday", "Monday"),
        ("tuesday", "Tuesday"),
        ("wednesday", "Wednesday"),
        ("thursday", "Thursday"),
        ("friday", "Friday"),
        ("saturday", "Saturday"),
        ("sunday", "Sunday"),
    ]

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    exercises = models.ManyToManyField(ExerciseMovement, blank=True)

    def get_day_display_name(self):
        return dict(self.DAY_CHOICES).get(self.day, self.day)

    def __str__(self):
        return f"{self.get_day_display_name()} Plan"


class ExercisePlan(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    daily_plans = models.ManyToManyField(DailyPlan, blank=True)
    goal = models.CharField(max_length=140, blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    plan_duration = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
