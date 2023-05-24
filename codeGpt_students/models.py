from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(default="-",max_length=11)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=13)
    collegeName = models.CharField(max_length=150)
    courseName = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    token = models.JSONField(default=dict)
    device = models.JSONField(default=dict)

class Students_Status(models.Model):
    refresnce_student_id = models.IntegerField(null=False)


class Question(models.Model):
    language = models.CharField(max_length=20)
    category = models.CharField(max_length=150)
    level = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    testcases = models.JSONField()
    expected = models.JSONField()
    example = models.CharField(max_length=100,default="")
    exp_inputs = models.CharField(max_length=100,default="")
    exp_outputs = models.CharField(max_length=100,default="")
    constraint = models.CharField(max_length=100,default=None)

