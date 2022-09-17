from django.db import models

# Create your models here.


class verification(models.Model):
    enrollment_no=models.CharField(max_length=20)
    fullname=models.CharField(max_length=20)
    fathername=models.CharField(max_length=50)
    starts_on=models.CharField(max_length=100)
    ends_on=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)

    def __str__(self):
        return self.enrollment_no