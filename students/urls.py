from django.urls import path
from .views import StudentsView,AddStudentView
app_name="students"
urlpatterns = [
    path('students/',StudentsView.as_view(),name="student"),
    path('students/add/',AddStudentView.as_view(),name="add-student")
]