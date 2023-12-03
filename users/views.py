from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import models
from .models import (
    UserExtra,
    TeacherExtra,
    UserCurrent,
    ExercisePlan,
    Movement,
    ExerciseMovement,
    DailyPlanExercise,
    Food,
    DailyPlanFood,
    FoodPlan,
)

# Create your views here.


def user_home(request):
    return render(request, "users/home.html")


def user_diet(request):
    return render(request, "users/mydiet.html")


def user_profile(request):
    user = request.user
    user_extra = UserExtra.objects.get(user=user)
    if request.method == "GET":
        return render(
            request,
            "users/profile.html",
            {
                "user": user,
                "user_extra": user_extra,
            },
        )
    elif request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")

        phone_number = request.POST.get("phone_number")
        birth_date = request.POST.get("birth_date")
        gender = request.POST.get("gender")
        profile_picture = request.FILES.get("profile_picture")

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.save()

        user_extra.phone_number = phone_number
        user_extra.birth_date = birth_date
        user_extra.gender = gender
        if profile_picture:
            user_extra.profile_picture = profile_picture
        user_extra.save()

        return render(
            request,
            "users/profile.html",
            {
                "user": user,
                "user_extra": user_extra,
            },
        )


def teacher_home(request):
    return render(request, "users/teachersHome.html")


def teachers_students(request):
    teacher = request.user
    teacher_extra = TeacherExtra.objects.get(user=teacher)
    if request.method == "GET":
        students = teacher_extra.students.all()
        students_extra = UserExtra.objects.filter(user__in=students)
        return render(
            request,
            "users/teachersStudent.html",
            {
                "teacher": teacher,
                "teacher_extra": teacher_extra,
                "students": students,
                "students_extra": students_extra,
            },
        )

    return render(request, "users/teachersStudent.html")


def teachers_students_info(request):
    student_id = request.GET.get("student_id")
    student_extra = get_object_or_404(UserExtra, user__id=student_id)
    student_current, created = UserCurrent.objects.get_or_create(
        user=student_extra.user
    )
    movements = Movement.objects.all()
    if request.method == "GET":
        return render(
            request,
            "users/teachersStudentInfo.html",
            {
                "student_extra": student_extra,
                "student_current": student_current,
                "movements": movements,
            },
        )

    elif request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "exercise_form":
            exercise_plan, created = ExercisePlan.objects.get_or_create(
                user=student_extra.user
            )
            daily_plan, created = DailyPlanExercise.objects.get_or_create(
                exerciseplan=exercise_plan
            )
            exercises, created = ExerciseMovement.objects.get_or_create(
                dailyplanexercise=daily_plan
            )
            movement_id = request.POST.get("movement_type")
            if movement_id:
                movement_type = Movement.objects.get(id=movement_id)
                exercises.movement_type = movement_type

            exercises.set_value = request.POST.get("set_value")
            exercises.repeat_value = request.POST.get("repeat_value")
            daily_plan.day = request.POST.get("day")
            exercise_plan.starting_date = request.POST.get("starting_date")
            exercise_plan.plan_duration = request.POST.get("program_duration")

            exercises.save()
            daily_plan.save()
            exercise_plan.save()
        elif form_type == "diet_form":
            food_plan, created = FoodPlan.objects.get_or_create(user=student_extra.user)
            diet_daily_plan, created = DailyPlanFood.objects.get_or_create(
                foodplan=food_plan
            )
            food, created = Food.objects.get_or_create(name=request.POST.get("food"))
            food_plan.cal_goal = request.POST.get("cal_goal")
            food_plan.goal = request.POST.get("diet_goal")

            meal_repast = request.POST.get("repast")

            if meal_repast == "breakfast":
                diet_daily_plan.breakfast_foods = food
            elif meal_repast == "lunch":
                diet_daily_plan.lunch_foods = food
            elif meal_repast == "dinner":
                diet_daily_plan.dinner_foods = food
            elif meal_repast == "snacks":
                diet_daily_plan.daily_snacks = food

            food.save()
            diet_daily_plan.save()
            food_plan.save()

        return render(
            request,
            "users/teachersStudentInfo.html",
            {
                "student_extra": student_extra,
                "student_current": student_current,
                "movements": movements,
            },
        )


def teacher_profile(request):
    teacher = request.user
    teacher_extra = TeacherExtra.objects.get(user=teacher)
    if request.method == "GET":
        return render(
            request,
            "users/teachersProfile.html",
            {
                "teacher": teacher,
                "teacher_extra": teacher_extra,
            },
        )
    elif request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        username = request.POST.get("username")

        phone_number = request.POST.get("phone_number")
        birth_date = request.POST.get("birth_date")
        gender = request.POST.get("gender")
        master_topic = request.POST.get("master_topic")
        experience = request.POST.get("experience")
        profile_picture = request.FILES.get("profile_picture")

        teacher.first_name = first_name
        teacher.last_name = last_name
        teacher.email = email
        teacher.username = username
        teacher.save()

        teacher_extra.phone_number = phone_number
        teacher_extra.birth_date = birth_date
        teacher_extra.gender = gender
        teacher_extra.master_topic = master_topic
        teacher_extra.experience = experience

        if profile_picture:
            teacher_extra.profile_picture = profile_picture
        teacher_extra.save()

        return render(
            request,
            "users/teachersProfile.html",
            {
                "teacher": teacher,
                "teacher_extra": teacher_extra,
            },
        )
