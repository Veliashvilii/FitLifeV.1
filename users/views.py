from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from . import models
from account.models import CustomUser
from .models import (
    UserExtra,
    TeacherExtra,
    UserCurrent,
    ExercisePlan,
    Movement,
    Food,
    FoodPlan,
    Message,
)

# Create your views here.


def user_home(request):
    user = request.user
    user_extra = UserExtra.objects.get(user=user)
    return render(
        request,
        "users/profile.html",
        {
            "user": user,
            "user_extra": user_extra,
        },
    )


def user_diet(request):
    user = request.user
    user_extra = UserExtra.objects.get(user=user)
    user_extra.current_info, created = UserCurrent.objects.get_or_create()
    user_extra.exercise_plan, created = ExercisePlan.objects.get_or_create()

    if request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "current_info":
            user_extra.current_info.weight_kg = request.POST.get("weight")
            user_extra.current_info.height_cm = request.POST.get("height")
            user_extra.current_info.body_fat_percentage = request.POST.get(
                "body_fat_percentage"
            )
            user_extra.current_info.muscle_mass_kg = request.POST.get("muscle_mass_kg")
            user_extra.current_info.bmi = request.POST.get("bmi")
            user_extra.current_info.save()
            return render(
                request,
                "users/mydiet.html",
                {
                    "user_extra": user_extra,
                    "user": user,
                    "user_extra.exercise_plan": user_extra.exercise_plan,
                },
            )

    return render(
        request,
        "users/mydiet.html",
        {
            "user_extra": user_extra,
            "user": user,
            "student_extra.exercise_plan": user_extra.exercise_plan,
        },
    )


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
    teacher = request.user
    teacher_extra, created = TeacherExtra.objects.get_or_create(user=teacher)
    return render(
        request,
        "users/teachersProfile.html",
        {
            "teacher": teacher,
            "teacher_extra": teacher_extra,
        },
    )


def teachers_students(request):
    teacher = request.user
    teacher_extra, created = TeacherExtra.objects.get_or_create(user=teacher)
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
    student_extra, created = UserExtra.objects.get_or_create(user__id=student_id)
    student_extra.current_info, created = UserCurrent.objects.get_or_create()
    student_extra.exercise_plan, created = ExercisePlan.objects.get_or_create()
    movements = Movement.objects.all()
    foods = Food.objects.all()
    if request.method == "GET":
        return render(
            request,
            "users/teachersStudentInfo.html",
            {
                "student_extra": student_extra,
                "student_current": student_extra.current_info,
                "movements": movements,
                "student_extra.exercise_plan": student_extra.exercise_plan,
                "foods": foods,
            },
        )
    elif request.method == "POST":
        form_type = request.POST.get("form_type")
        if form_type == "exercise_form":
            student_id = request.GET.get("student_id")
            student_extra, created = UserExtra.objects.get_or_create(
                user__id=student_id
            )
            student_extra.exercise_plan, created = ExercisePlan.objects.get_or_create()
            student_extra.food_plan, created = FoodPlan.objects.get_or_create()

            monday_movement_id = request.POST.get("movement_type_monday")
            tuesday_movement_id = request.POST.get("movement_type_tuesday")
            wednesday_movement_id = request.POST.get("movement_type_wednesday")
            thursday_movement_id = request.POST.get("movement_type_thursday")
            friday_movement_id = request.POST.get("movement_type_friday")
            saturday_movement_id = request.POST.get("movement_type_saturday")
            sunday_movement_id = request.POST.get("movement_type_sunday")

            monday_set_id = request.POST.get("set_value_monday")
            tuesday_set_id = request.POST.get("set_value_tuesday")
            wednesday_set_id = request.POST.get("set_value_wednesday")
            thursday_set_id = request.POST.get("set_value_thursday")
            friday_set_id = request.POST.get("set_value_friday")
            saturday_set_id = request.POST.get("set_value_saturday")
            sunday_set_id = request.POST.get("set_value_sunday")

            monday_repeat_id = request.POST.get("repeat_value_monday")
            tuesday_repeat_id = request.POST.get("repeat_value_tuesday")
            wednesday_repeat_id = request.POST.get("repeat_value_wednesday")
            thursday_repeat_id = request.POST.get("repeat_value_thursday")
            friday_repeat_id = request.POST.get("repeat_value_friday")
            saturday_repeat_id = request.POST.get("repeat_value_saturday")
            sunday_repeat_id = request.POST.get("repeat_value_sunday")

            if monday_movement_id != 0:
                student_extra.exercise_plan.monday = Movement.objects.get(
                    id=monday_movement_id
                )
                student_extra.exercise_plan.monday.set_value = monday_set_id
                student_extra.exercise_plan.monday.repeat_value = monday_repeat_id

            if tuesday_movement_id != 0:
                student_extra.exercise_plan.tuesday = Movement.objects.get(
                    id=tuesday_movement_id
                )
                student_extra.exercise_plan.tuesday.set_value = tuesday_set_id
                student_extra.exercise_plan.tuesday.repeat_value = tuesday_repeat_id

            if wednesday_movement_id != 0:
                student_extra.exercise_plan.wednesday = Movement.objects.get(
                    id=wednesday_movement_id
                )
                student_extra.exercise_plan.wednesday.set_value = wednesday_set_id
                student_extra.exercise_plan.wednesday.repeat_value = wednesday_repeat_id

            if thursday_movement_id != 0:
                student_extra.exercise_plan.thursday = Movement.objects.get(
                    id=thursday_movement_id
                )
                student_extra.exercise_plan.thursday.set_value = thursday_set_id
                student_extra.exercise_plan.thursday.repeat_value = thursday_repeat_id

            if friday_movement_id != 0:
                student_extra.exercise_plan.friday = Movement.objects.get(
                    id=friday_movement_id
                )
                student_extra.exercise_plan.friday.set_value = friday_set_id
                student_extra.exercise_plan.friday.repeat_value = friday_repeat_id

            if saturday_movement_id != 0:
                student_extra.exercise_plan.saturday = Movement.objects.get(
                    id=saturday_movement_id
                )
                student_extra.exercise_plan.saturday.set_value = saturday_set_id
                student_extra.exercise_plan.saturday.repeat_value = saturday_repeat_id

            if sunday_movement_id != 0:
                student_extra.exercise_plan.sunday = Movement.objects.get(
                    id=sunday_movement_id
                )
                student_extra.exercise_plan.sunday.set_value = sunday_set_id
                student_extra.exercise_plan.sunday.repeat_value = sunday_repeat_id

            student_extra.exercise_plan.save()

            return render(
                request,
                "users/teachersStudentInfo.html",
                {
                    "student_extra": student_extra,
                    "student_current": student_extra.current_info,
                    "movements": movements,
                    "student_extra.exercise_plan": student_extra.exercise_plan,
                    "foods": foods,
                },
            )
        if form_type == "complate_exercise":
            student_id = request.GET.get("student_id")
            student_extra, created = UserExtra.objects.get_or_create(
                user__id=student_id
            )
            student_extra.exercise_plan, created = ExercisePlan.objects.get_or_create()
            student_extra.exercise_plan.goal = request.POST.get("plan_goal")
            student_extra.exercise_plan.starting_date = request.POST.get(
                "starting_date"
            )
            student_extra.exercise_plan.plan_duration = request.POST.get(
                "program_duration"
            )
            student_extra.exercise_plan.save()

            return render(
                request,
                "users/teachersStudentInfo.html",
                {
                    "student_extra": student_extra,
                    "student_current": student_extra.current_info,
                    "movements": movements,
                    "student_extra.exercise_plan": student_extra.exercise_plan,
                    "foods": foods,
                },
            )
        if form_type == "diet_plan":
            student_id = request.GET.get("student_id")
            student_extra, created = UserExtra.objects.get_or_create(
                user__id=student_id
            )
            student_extra.food_plan, created = FoodPlan.objects.get_or_create()

            for meal_type in ["breakfast", "lunch", "dinner", "snacks"]:
                for day in [
                    "monday",
                    "tuesday",
                    "wednesday",
                    "thursday",
                    "friday",
                    "saturday",
                    "sunday",
                ]:
                    field_name = f"{meal_type}_{day}"
                    food_id = request.POST.get(field_name)

                    if food_id:
                        student_extra.food_plan.set_meal(day, meal_type, food_id)

            student_extra.food_plan.save()

            return render(
                request,
                "users/teachersStudentInfo.html",
                {
                    "student_extra": student_extra,
                    "student_current": student_extra.current_info,
                    "movements": movements,
                    "student_extra.exercise_plan": student_extra.exercise_plan,
                    "foods": foods,
                },
            )


def teacher_profile(request):
    teacher = request.user
    teacher_extra, created = TeacherExtra.objects.get_or_create(user=teacher)
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


def message_view_student(request):
    if request.method == "POST":
        sender = request.user
        sender_extra = UserExtra.objects.get(user=sender)
        content = request.POST.get("content")

        receiver = CustomUser.objects.get(id=sender_extra.trainer.id)

        Message.objects.create(sender=request.user, receiver=receiver, content=content)

    messages = Message.objects.filter(sender=request.user) | Message.objects.filter(
        receiver=request.user
    )

    return render(request, "users/messages.html", {"messages": messages})


def message_view_teacher(request):
    sender = request.user
    sender_extra = TeacherExtra.objects.get(user=sender)

    if request.method == "GET":
        students = sender_extra.students.all()
        students_extra = UserExtra.objects.filter(user__in=students)
        global obj
        obj = students_extra

        return render(
            request,
            "users/messagesTeacher.html",
            {
                "sender": sender,
                "sender_extra": sender_extra,
                "students": students,
                "students_extra": students_extra,
            },
        )


def message_teacher_send(request):
    sender = request.user
    sender_extra = TeacherExtra.objects.get(user=sender)
    student_extra = obj

    if request.method == "GET":
        return render(
            request,
            "users/messagesTeacherSend.html",
            {
                "sender": sender,
                "sender_extra": sender_extra,
            },
        )
    elif request.method == "POST":
        content = request.POST.get("content")

        Message.objects.create(sender=request.user, receiver=receiver, content=content)

        messages = Message.objects.filter(sender=request.user) | Message.objects.filter(
            receiver=request.user
        )

        return render(
            request,
            "users/messagesTeacherSend.html",
            {
                "sender": sender,
                "sender_extra": sender_extra,
                "student_extra": student_extra,
                "messages": messages,
            },
        )
