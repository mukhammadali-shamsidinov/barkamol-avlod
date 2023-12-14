from django.db import models

from facultet.models import Facultet


# Create your models here.

class Achivments(models.Model):
    sertificate = models.FileField(upload_to='student-achivments/')
    stipend = models.DecimalField(max_digits=10,decimal_places=2)
    other = models.FileField(upload_to='student-achivments/')


class Classes(models.Model):
    name = models.CharField(max_length=2)
    C = (
        ('A','A'),
        ('B','B'),
        ('C','C')
    )
    type = models.CharField(choices=C)

    def __str__(self):
        return f"{self.name} {self.type}"



class StudentParents(models.Model):
    father_name = models.CharField(max_length=128)
    father_date_of_birth = models.DateTimeField()
    Jobs_Father = (
        ('actor','actor'),
        ('singer','singer'),
        ('detective','detective'),
        ('butcher','butcher'),
        ('programmer','programmer')
    )
    father_job = models.CharField(choices=Jobs_Father)
    mather_name = models.CharField(max_length=128)
    mather_date_of_birth = models.DateTimeField()
    Jobs_Mather = (
        ('norse','norse'),
        ('actress','actress')
    )
    mather_of_job = models.CharField(choices=Jobs_Mather)

    def __str__(self):
        return f"{self.father_name} and {self.mather_name}"


class StudentSos(models.Model):
    name = models.CharField()
    Relation = (
        ('Brother','Brother'),
        ('Sister','Sister'),
        ('father','father'),
        ('mather','mather')
    )
    relation_ship = models.CharField(choices=Relation)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=13)
    birth_date = models.DateTimeField()
    facultet = models.ForeignKey(Facultet,on_delete=models.CASCADE)
    gender_status = (
        ('male','male'),
        ('female','female'),
        ('other','other')
    )
    Notions = (
        ('Germany','Germany'),
        ('Spain', 'Spain'),
        ('Uzbekistan', 'Uzbekistan'),
        ('Tojikiston', 'Tojikiston'),
    )
    gender = models.CharField(choices=gender_status)
    notions = models.CharField(choices=Notions)
    img = models.ImageField(upload_to='student-images/')
    contract = models.DecimalField(max_digits=10,decimal_places=2)
    achivments = models.ForeignKey(Achivments,on_delete=models.CASCADE,related_name='achivments',blank=True,null=True)
    call_sos = models.ForeignKey(StudentSos,on_delete=models.CASCADE,null=True,blank=True)
    parents = models.ForeignKey(StudentParents,on_delete=models.CASCADE,blank=True,null=True)
    STATUS=(
        ('process','process'),
        ('pending','pending'),
        ('success','success')
    )
    status = models.CharField(choices=STATUS,default='process')
    classes = models.ForeignKey(Classes,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.first_name} {self.facultet.name}"

