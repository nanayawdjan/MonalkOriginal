from django.db import models
from django.contrib.auth.models import User
# Create your models here.


COMING_FROM = [
    ('Dwenem','Dwenem'),
    ('Mpuasu','Mpuasu'),
    ('Adamsu','Adamsu'),
    ('Bodaa','Bodaa'),
    ('Kofitia','Kofitia'),
    ('Adiokor1','Adiokor1'),
    ('Adiokor2','Adiokor2'),
    ('Zezera','Zezera'),
    ('Kwamepim','Kwamepim'),
]

GENDER = [
    ('Male','Male'),
    ('Female','Female')
]

classes=[
    ('F & B','F & B'),
    ('P.S.','P.S.'),
    ('K.S.A.','K.S.A.'),
    ('K.S.B.','K.S.B.'),
    ('K.S.C.','K.S.C.'),
    ('L.S.A.','L.S.A.'),
]


class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    passport = models.ImageField(blank=True, null=True, upload_to="static/images/passports/")
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name



class StudentExtra(models.Model):
    roll = models.CharField(max_length=10)
    date_of_admission = models.DateField(null=True, blank=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=45, null=True, choices=GENDER)
    mother = models.CharField(max_length=45, null=True, blank=True)
    father = models.CharField(max_length=45, null=True, blank=True)
    mobile = models.CharField(max_length=40,null=True, blank=True)
    cl= models.CharField(max_length=10,choices=classes,default='one')
    residence = models.CharField(max_length=45, null=True, choices=COMING_FROM)
    fee=models.FloatField(null=True)
    status=models.BooleanField(default=False)
    passport = models.ImageField(blank=True, null=True, upload_to="static/images/passports/")
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Payment(models.Model):
    student = models.ForeignKey(StudentExtra, null=True, on_delete=models.SET_NULL) 
    pay = models.FloatField(default=0, null=True, blank=True)
    when_made = models.DateField(blank=True, null=True)
    balance = models.FloatField(default=0, null=True, blank=True)
    depth = models.FloatField(default=0, null=True, blank=True)


class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)
