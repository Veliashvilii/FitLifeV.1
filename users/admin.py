from django.contrib import admin
from .models import (
    UserExtra,
    UserCurrent,
    Movement,
    DailyPlan,
    ExerciseMovement,
    ExercisePlan,
)

# Register your models here.
admin.site.register(UserExtra)
admin.site.register(UserCurrent)
admin.site.register(Movement)
admin.site.register(ExercisePlan)
admin.site.register(ExerciseMovement)
admin.site.register(DailyPlan)
