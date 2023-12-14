from django import forms

from students.models import Student


class AddStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'