from django.db import models

from students.models import Student


class Teachers(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone_num = models.CharField(max_length=12)
    Speices = (
        ('math','math'),
        ('geograpia','geograpia'),
        ('algebra','algebra')
    )
    specs = models.CharField(choices=Speices)
    email = models.EmailField()
    cost = models.DecimalField(max_digits=10,decimal_places=2)
    img = models.ImageField(upload_to='teachers/')
    def __str__(self):
        return self.first_name




# Create your models here.
class Academic(models.Model):
    teacher = models.ForeignKey(Teachers,on_delete=models.CASCADE,related_name='teacher')
    students = models.ForeignKey(Student,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_name.name} {self.class_name.type} {self.students.first_name} {self.students.facultet.name}"
