from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from account.models import CustomUser


class Movement(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    goal = models.CharField(max_length=140, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    set_value = models.IntegerField(blank=True, null=True)
    repeat_value = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


class ExercisePlan(models.Model):
    monday = models.OneToOneField(
        Movement,
        blank=True,
        related_name="monday_exercise",
        null=True,
        on_delete=models.CASCADE,
    )
    tuesday = models.OneToOneField(
        Movement,
        blank=True,
        related_name="tuesday_exercise",
        null=True,
        on_delete=models.CASCADE,
    )
    wednesday = models.OneToOneField(
        Movement,
        blank=True,
        related_name="wednesday_exercise",
        null=True,
        on_delete=models.CASCADE,
    )
    thursday = models.OneToOneField(
        Movement,
        blank=True,
        related_name="thursday_exercise",
        null=True,
        on_delete=models.CASCADE,
    )
    friday = models.OneToOneField(
        Movement,
        blank=True,
        related_name="friday_exercise",
        null=True,
        on_delete=models.CASCADE,
    )
    saturday = models.OneToOneField(
        Movement,
        blank=True,
        related_name="saturday_exercise",
        null=True,
        on_delete=models.CASCADE,
    )
    sunday = models.OneToOneField(
        Movement,
        blank=True,
        related_name="sunday_exercise",
        null=True,
        on_delete=models.CASCADE,
    )
    goal = models.CharField(max_length=140, blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    plan_duration = models.CharField(max_length=60, blank=True, null=True)


class Food(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    calory = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class FoodPlan(models.Model):
    goal = models.CharField(max_length=140, blank=True, null=True)
    cal_goal = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    monday_breakfast = models.OneToOneField(
        Food,
        blank=True,
        related_name="monday_food_breakfast",
        null=True,
        on_delete=models.CASCADE,
    )
    monday_lunch = models.OneToOneField(
        Food,
        blank=True,
        related_name="monday_food_lunch",
        null=True,
        on_delete=models.CASCADE,
    )
    monday_dinner = models.OneToOneField(
        Food,
        blank=True,
        related_name="monday_food_dinner",
        null=True,
        on_delete=models.CASCADE,
    )
    monday_snacks = models.OneToOneField(
        Food,
        blank=True,
        related_name="monday_food_snacks",
        null=True,
        on_delete=models.CASCADE,
    )
    tuesday_breakfast = models.OneToOneField(
        Food,
        blank=True,
        related_name="tuesday_food_breakfast",
        null=True,
        on_delete=models.CASCADE,
    )
    tuesday_lunch = models.OneToOneField(
        Food,
        blank=True,
        related_name="tuesday_food_lunch",
        null=True,
        on_delete=models.CASCADE,
    )
    tuesday_dinner = models.OneToOneField(
        Food,
        blank=True,
        related_name="tuesday_food_dinner",
        null=True,
        on_delete=models.CASCADE,
    )
    tuesday_snacks = models.OneToOneField(
        Food,
        blank=True,
        related_name="tuesday_food_snacks",
        null=True,
        on_delete=models.CASCADE,
    )
    wednesday_breakfast = models.OneToOneField(
        Food,
        blank=True,
        related_name="wednesday_food_breakfast",
        null=True,
        on_delete=models.CASCADE,
    )
    wednesday_lunch = models.OneToOneField(
        Food,
        blank=True,
        related_name="wednesday_food_lunch",
        null=True,
        on_delete=models.CASCADE,
    )
    wednesday_dinner = models.OneToOneField(
        Food,
        blank=True,
        related_name="wednesday_food_dinner",
        null=True,
        on_delete=models.CASCADE,
    )
    wednesday_snacks = models.OneToOneField(
        Food,
        blank=True,
        related_name="wednesday_food_snacks",
        null=True,
        on_delete=models.CASCADE,
    )
    thursday_breakfast = models.OneToOneField(
        Food,
        blank=True,
        related_name="thursday_food_breakfast",
        null=True,
        on_delete=models.CASCADE,
    )
    thursday_lunch = models.OneToOneField(
        Food,
        blank=True,
        related_name="thursday_food_lunch",
        null=True,
        on_delete=models.CASCADE,
    )
    thursday_dinner = models.OneToOneField(
        Food,
        blank=True,
        related_name="thursday_food_dinner",
        null=True,
        on_delete=models.CASCADE,
    )
    thursday_snacks = models.OneToOneField(
        Food,
        blank=True,
        related_name="thursday_food_snacks",
        null=True,
        on_delete=models.CASCADE,
    )
    friday_breakfast = models.OneToOneField(
        Food,
        blank=True,
        related_name="friday_food_breakfast",
        null=True,
        on_delete=models.CASCADE,
    )
    friday_lunch = models.OneToOneField(
        Food,
        blank=True,
        related_name="friday_food_lunch",
        null=True,
        on_delete=models.CASCADE,
    )
    friday_dinner = models.OneToOneField(
        Food,
        blank=True,
        related_name="friday_food_dinner",
        null=True,
        on_delete=models.CASCADE,
    )
    friday_snacks = models.OneToOneField(
        Food,
        blank=True,
        related_name="friday_food_snacks",
        null=True,
        on_delete=models.CASCADE,
    )
    saturday_breakfast = models.OneToOneField(
        Food,
        blank=True,
        related_name="saturday_food_breakfast",
        null=True,
        on_delete=models.CASCADE,
    )
    saturday_lunch = models.OneToOneField(
        Food,
        blank=True,
        related_name="saturday_food_lunch",
        null=True,
        on_delete=models.CASCADE,
    )
    saturday_dinner = models.OneToOneField(
        Food,
        blank=True,
        related_name="saturday_food_dinner",
        null=True,
        on_delete=models.CASCADE,
    )
    saturday_snacks = models.OneToOneField(
        Food,
        blank=True,
        related_name="saturday_food_snacks",
        null=True,
        on_delete=models.CASCADE,
    )
    sunday_breakfast = models.OneToOneField(
        Food,
        blank=True,
        related_name="sunday_food_breakfast",
        null=True,
        on_delete=models.CASCADE,
    )
    sunday_lunch = models.OneToOneField(
        Food,
        blank=True,
        related_name="sunday_food_lunch",
        null=True,
        on_delete=models.CASCADE,
    )
    sunday_dinner = models.OneToOneField(
        Food,
        blank=True,
        related_name="sunday_food_dinner",
        null=True,
        on_delete=models.CASCADE,
    )
    sunday_snacks = models.OneToOneField(
        Food,
        blank=True,
        related_name="sunday_food_snacks",
        null=True,
        on_delete=models.CASCADE,
    )

    def set_meal(self, day, meal_type, food_id):
        meal_key = f"{meal_type}_{day}"
        food_key = f"{meal_type}_food_{day}"

        food = Food.objects.get(id=food_id)

        setattr(self, food_key, food)
        self.save()


class UserCurrent(models.Model):
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
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
    )

    trainer = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_trainer",
        limit_choices_to={"is_user": 0},
    )

    exercise_plan = models.OneToOneField(
        ExercisePlan, on_delete=models.CASCADE, null=True, blank=True
    )

    current_info = models.OneToOneField(
        UserCurrent, on_delete=models.CASCADE, null=True, blank=True
    )

    food_plan = models.OneToOneField(
        FoodPlan, on_delete=models.CASCADE, null=True, blank=True
    )

    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Message(models.Model):
    sender = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="received_messages"
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} to {self.receiver.username} - {self.timestamp}"
