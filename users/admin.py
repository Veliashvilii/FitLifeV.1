from django.contrib import admin
from account.models import CustomUser
from .models import (
    UserExtra,
    UserCurrent,
    Movement,
    DailyPlanExercise,
    ExerciseMovement,
    ExercisePlan,
    Food,
    DailyPlanFood,
    FoodPlan,
)

# Register your models here.
admin.site.register(UserExtra)
admin.site.register(UserCurrent)
admin.site.register(Movement)
admin.site.register(ExercisePlan)
admin.site.register(ExerciseMovement)
admin.site.register(DailyPlanExercise)
admin.site.register(Food)
admin.site.register(DailyPlanFood)
admin.site.register(FoodPlan)
admin.site.register(CustomUser)
