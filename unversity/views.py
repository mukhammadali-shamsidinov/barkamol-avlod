from django.shortcuts import render

from academic.models import Teachers
from students.models import Student, Classes
from users.models import CustomUser


def landing(request):
    teachers = Teachers.objects.all().count()
    students = Student.objects.all().count()
    classes = Classes.objects.all().count()
    user = CustomUser.objects.all().count()
    context = {
        "user":user,
        "teacher_count":teachers,
        "students_count":students,
        "classes_count":classes,
        "users_count":user
    }
    return render(request,'index.html',context)