from django.contrib import admin
from account.models import CustomUser
from .models import (
    UserExtra,
    UserCurrent,
    Movement,
    ExercisePlan,
    Food,
    FoodPlan,
    TeacherExtra,
)

# Register your models here.
admin.site.register(UserExtra)
admin.site.register(UserCurrent)
admin.site.register(Movement)
admin.site.register(ExercisePlan)
admin.site.register(Food)
admin.site.register(FoodPlan)
admin.site.register(CustomUser)
admin.site.register(TeacherExtra)
