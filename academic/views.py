from django.shortcuts import render
from django.views import View

from academic.models import Teachers


# Create your views here.
class TeachersView(View):
    def get(self,request):
        teachers = Teachers.objects.all()
        return render(request,'teachers.html',{"teachers":teachers})

class TeacherDetailView(View):
    def get(self,request,id):
        teacher = Teachers.objects.get(id=id)
        return render(request,'teacher-detail.html',{"teacher":teacher})