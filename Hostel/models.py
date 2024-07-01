from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)



class student(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)
    parent_name = models.CharField(max_length=100,null=True)
    parent_contact = models.CharField(max_length=100,null=True)



class Hostel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    owner = models.CharField(max_length=100,null=True)
    gender = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to='media/', null=True)
    hostel_category = models.CharField(max_length=100,null=True)



class room(models.Model):
    room_number=models.CharField(max_length=100,null=True)
    room_type = models.CharField(max_length=100,null=True)
    block = models.CharField(max_length=100,null=True)

class book(models.Model):
    hostel = models.ForeignKey(Hostel,on_delete=models.CASCADE,null=True)
    guest = models.ForeignKey(student,on_delete=models.CASCADE,null=True)
    room = models.ForeignKey(room,on_delete=models.CASCADE,null=True)

    Check_in= models.DateField(max_length=100,null=True)
    Duration = models.CharField(max_length=100,null=True)
    Total = models.IntegerField(max_length=100,null=True)
    status = models.CharField(max_length=100,null=True)

    payment=models.CharField(max_length=100,null=True)
class Room_alocate(models.Model):
    guest = models.ForeignKey(student,on_delete=models.CASCADE,null=True)
    room = models.ForeignKey(room,on_delete=models.CASCADE,null=True)
    
class Attendance(models.Model):
    ab_date = models.CharField(max_length=100)
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    ab_status = models.CharField(max_length=100)
class LeaveApply(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    leave_from = models.CharField(max_length=100)
    leave_till = models.CharField(max_length=100)
    status = models.CharField(max_length=100)