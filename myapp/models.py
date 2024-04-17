from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)

class Expert(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    specialization=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)

class Staff(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    pin=models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,default=1)

class Driver(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    licenseno=models.CharField(max_length=50)
    lattitude=models.CharField(max_length=50,default=1)
    longitude=models.CharField(max_length=50,default=1)

class bus(models.Model):
    vehicleno=models.CharField(max_length=50)

class Busassign_driver(models.Model):
    DRIVER=models.ForeignKey(Driver,on_delete=models.CASCADE)
    BUS=models.ForeignKey(bus,on_delete=models.CASCADE)

class Student(models.Model):
    STAFF=models.ForeignKey(Staff,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    pin=models.CharField(max_length=50)
    clas=models.CharField(max_length=50)
    division=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,default=1)
    dob=models.CharField(max_length=50,default=1)

class parent(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    pin=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)


class Busassign_student(models.Model):
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)
    BUS=models.ForeignKey(bus,on_delete=models.CASCADE)

class attendence(models.Model):
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)
    date=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default=1)

class Tips(models.Model):
    EXPERT=models.ForeignKey(Expert,on_delete=models.CASCADE)
    tips=models.CharField(max_length=50)
    date=models.CharField(max_length=50)

class childassign(models.Model):
    PARENT=models.ForeignKey(parent,on_delete=models.CASCADE)
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)

class notification(models.Model):
    DRIVER=models.ForeignKey(Driver,on_delete=models.CASCADE)
    notification=models.CharField(max_length=50)
    date=models.CharField(max_length=50)

class work(models.Model):
    STAFF=models.ForeignKey(Staff,on_delete=models.CASCADE)
    work=models.CharField(max_length=50)
    date=models.CharField(max_length=50)

class assign_work(models.Model):
    STUDENT=models.ForeignKey(Student,on_delete=models.CASCADE)
    WORK=models.ForeignKey(work,on_delete=models.CASCADE)
    status=models.CharField(max_length=50)
    date=models.CharField(max_length=50)


class performance(models.Model):
    photo=models.CharField(max_length=250)
    STAFF = models.ForeignKey(Staff, on_delete=models.CASCADE)
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    date=models.CharField(max_length=250)

class note(models.Model):
    photo = models.CharField(max_length=250)
    STAFF = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.CharField(max_length=250)

class locate(models.Model):
    DRIVER = models.ForeignKey(Driver, on_delete=models.CASCADE)
    lattitude = models.CharField(max_length=50, default=1)
    longitude = models.CharField(max_length=50, default=1)



class chat(models.Model):
    PARENT = models.ForeignKey(parent, on_delete=models.CASCADE)
    EXPERT = models.ForeignKey(Expert, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    type = models.CharField(max_length=255, default=1)

class std_status(models.Model):
    STUDENT = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    DRIVER = models.ForeignKey(Driver, on_delete=models.CASCADE,default=1)














