from django.urls import path
from .views import TeachersView,TeacherDetailView
app_name="academic"
urlpatterns = [
    path('all/',TeachersView.as_view(),name="teachers_all"),
    path('teacher/<int:id>/',TeacherDetailView.as_view(),name="teacher_detail")
]