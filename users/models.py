from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='users/',default='6.jpg')
    AUTH_STATUS = (
        ('ordernary','ordernary'),
        ('manager', 'manager'),
        ('admin', 'admin'),
    )
    JOB=(
        ('Frontend','Frontend'),
        ('Backend','Backend'),
        ('FullStack', 'FullStack'),
    )
    job = models.CharField(choices=JOB)

    auth_status = models.CharField(choices=AUTH_STATUS,default='ordernary')
