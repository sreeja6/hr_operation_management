from django.db import models
class Employee(models.Model):
    emp_no = models.AutoField(primary_key = True)
    emp_name = models.CharField(max_length=30)
    emp_password = models.CharField(max_length=15)
    emp_designation = models.CharField(max_length=20)
    emp_adress = models.CharField(max_length=50)
    emp_contact = models.IntegerField(max_length=10)
    emp_email = models.EmailField()

class recurt(models.Model):
    rno = models.AutoField(primary_key = True)
    oppcode = models.IntegerField(unique=True)
    quali = models.CharField(max_length=30)
    startdate = models.CharField(max_length=20)
    age = models.IntegerField()
    lastdate = models.CharField(max_length=20)
    deptid = models.CharField(max_length=10)
    position = models.IntegerField()
    des = models.CharField(max_length=30)
    res = models.CharField(max_length=50)
    cno = models.IntegerField(max_length=10)
class InterviewSchedule(models.Model):
    applicant_id = models.IntegerField()
    emp_id = models.IntegerField()
    schedule_date = models.CharField(max_length=30)
class ApplicantRegisteration(models.Model):

     id = models.AutoField(primary_key=True)
     name = models.CharField(max_length=30)
     date_of_birth = models.CharField(max_length=20)
     email = models.EmailField(unique=True)
     gender = models.CharField(max_length=8)
     mobile_no = models.IntegerField()
     Adress = models.CharField(max_length=40)
     username = models.CharField(max_length=15)
     password = models.CharField(max_length=15)


class Applicant_Application_form(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    date_of_birth = models.CharField(max_length=20)
    email = models.EmailField()
    gender = models.CharField(max_length=8)
    mobile_no = models.IntegerField(max_length=10)
    Adress = models.CharField(max_length=40)
    qualifaction = models.CharField(max_length=10)
    post = models.CharField(max_length=20)
    percentage = models.IntegerField()
    resume = models.FileField(upload_to='applicant_resume/')
class Finalized_candiadates(models.Model):
    f_applicant_id = models.IntegerField(unique=True)
    f_emp_id = models.IntegerField()
    f_schedule_date = models.CharField(max_length=30)
    result = models.CharField(max_length=18)




