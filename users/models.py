from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from account.models import CustomUser


class TeacherExtra(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    students = models.ManyToManyField(
        CustomUser,
        related_name="teachers",
        blank=True,
        limit_choices_to={"is_user": 1},
    )

    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="images", default="")
    master_topic = models.CharField(max_length=60, null=True, blank=True)
    experience = models.CharField(max_length=140, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class UserExtra(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    trainer = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_trainer",
        limit_choices_to={"is_user": 0},
    )
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class UserCurrent(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
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
    movement_type = models.OneToOneField(
        Movement, on_delete=models.CASCADE, blank=True, null=True
    )
    set_value = models.IntegerField(blank=True, null=True)
    repeat_value = models.IntegerField(blank=True, null=True)

    def get_movement_name(self):
        if self.movement_type.exists():
            return self.movement_type.last().name
        else:
            return "No Movement Selected"

    def __str__(self):
        return f"{self.get_movement_name()}"


class DailyPlanExercise(models.Model):
    DAY_CHOICES = [
        ("monday", "Monday"),
        ("tuesday", "Tuesday"),
        ("wednesday", "Wednesday"),
        ("thursday", "Thursday"),
        ("friday", "Friday"),
        ("saturday", "Saturday"),
        ("sunday", "Sunday"),
    ]

    day = models.CharField(max_length=10, choices=DAY_CHOICES, blank=True)
    exercises = models.ManyToManyField(ExerciseMovement, blank=True)

    def get_day_display_name(self):
        return dict(self.DAY_CHOICES).get(self.day, self.day)

    def __str__(self):
        return f"{self.get_day_display_name()} Plan"


class ExercisePlan(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    daily_plans = models.ManyToManyField(DailyPlanExercise, blank=True)
    goal = models.CharField(max_length=140, blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    plan_duration = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Food(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class DailyPlanFood(models.Model):
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
    breakfast_foods = models.OneToOneField(
        Food,
        related_name="breakfast_foods",
        blank=True,
        on_delete=models.CASCADE,
        null=True,
    )
    lunch_foods = models.OneToOneField(
        Food,
        related_name="lunch_foods",
        blank=True,
        on_delete=models.CASCADE,
        null=True,
    )
    dinner_foods = models.OneToOneField(
        Food,
        related_name="dinner_foods",
        blank=True,
        on_delete=models.CASCADE,
        null=True,
    )
    daily_snacks = models.OneToOneField(
        Food,
        related_name="daily_foods",
        blank=True,
        on_delete=models.CASCADE,
        null=True,
    )

    def get_day_display_name(self):
        return dict(self.DAY_CHOICES).get(self.day, self.day)

    def __str__(self):
        return f"{self.get_day_display_name()} Plan"


class FoodPlan(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    daily_plans = models.ManyToManyField(DailyPlanFood, blank=True)
    goal = models.CharField(max_length=140, blank=True, null=True)
    cal_goal = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
