from django.contrib import admin
from .models import Student,StudentParents,Achivments,Classes
# Register your models here.
admin.site.register(Student)
admin.site.register(StudentParents)
admin.site.register(Achivments)
admin.site.register(Classes)
