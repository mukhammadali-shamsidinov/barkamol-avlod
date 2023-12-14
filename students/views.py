from django.shortcuts import render, redirect
from django.views import View

from students.forms import AddStudentForm
from students.models import Student


# Create your views here.
class StudentsView(View):
    def get(self,request):
        query = self.request.GET.get("q",'')
        students = Student.objects.all().order_by('first_name')
        if query:
            students = students.filter(first_name__icontains=query)
        context = {
            "students":students
        }
        return render(request,'students.html',context)


class AddStudentView(View):
    def get(self,request):
        student_form = AddStudentForm()
        return render(request,'add-student.html',{"form":student_form})
    def post(self,request):
        student_form = AddStudentForm(data=request.POST,files=request.FILES)
        if student_form.is_valid():
            student_form.save()
            return redirect("students:student")
        else:
            return render(request, 'add-student.html', {"form": student_form})
