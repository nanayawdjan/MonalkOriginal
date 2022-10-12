from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.


COMING_FROM = [
    ('Dwenem', 'Dwenem'),
    ('Mpuasu', 'Mpuasu'),
    ('Adamsu', 'Adamsu'),
    ('Bodaa', 'Bodaa'),
    ('Kofitia', 'Kofitia'),
    ('Adiokor1', 'Adiokor1'),
    ('Adiokor2', 'Adiokor2'),
    ('Zezera', 'Zezera'),
    ('Kwamepim', 'Kwamepim'),
]

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

CLASSES = [
    ('F & B', 'F & B'),
    ('P.S.', 'P.S.'),
    ('K.S.A.', 'K.S.A.'),
    ('K.S.B.', 'K.S.B.'),
    ('K.S.C.', 'K.S.C.'),
    ('L.S.A.', 'L.S.A.'),
]

FORM_OF_TRANSPORTATION = [
    ('Bus', 'Bus'),
    ('Walk', 'Walk')
]

PAYMENT_METHOD = [
    ('Pay_Per_Day', 'Pay Per Day'),
    ('School_Fees_Aside', 'School Fees Aside')

]

PAYMENT_CATEGORY = [
    ('Pay_Everything', 'Pay Everything'),
    ('Dont_Pay', 'Don\'t Pay'),
    ('Considered', 'Considered'),
]


class TeacherExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate = models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status = models.BooleanField(default=False)
    passport = models.ImageField(
        blank=True, null=True, upload_to="static/images/passports/")

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=45, null=True, choices=GENDER)
    mother = models.CharField(max_length=45, null=True, blank=True)
    father = models.CharField(max_length=45, null=True, blank=True)
    mobile = models.CharField(max_length=40, null=True, blank=True)
    cl = models.CharField(max_length=10, choices=CLASSES, null=True)
    residence = models.CharField(max_length=45, null=True, choices=COMING_FROM)
    fee = models.FloatField(null=True, default=210)
    foodfee = models.FloatField(null=True, blank=True)
    carfee = models.FloatField(null=True, blank=True)
    status = models.BooleanField(default=False)
    checkifpaiddaily = models.BooleanField(default=False)
    checkifpaidterm = models.BooleanField(default=False)
    debt = models.FloatField(null=True, blank=True, default=0)
    balance = models.FloatField(null=True, blank=True, default=0)

    # ||||||||||||| ADDED ON 5TH OCTOBER ||||||||||||||||
    payment_category = models.CharField(
        max_length=40, choices=PAYMENT_CATEGORY, null=True)
    form_of_transportation = models.CharField(
        max_length=40, choices=FORM_OF_TRANSPORTATION, null=True)
    payment_method = models.CharField(
        max_length=40, choices=PAYMENT_METHOD, null=True)
    # ||||||||||||| ADDED ON 5TH OCTOBER ||||||||||||||||

    passport = models.ImageField(
        blank=True, null=True, upload_to="static/images/passports/")

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name+' '+self.user.last_name


class Payment(models.Model):
    student = models.ForeignKey(
        StudentExtra, null=True, on_delete=models.SET_NULL, blank=True)
    pay = models.FloatField(null=True, blank=True)
    carpay = models.FloatField(null=True, blank=True)
    schoolfees = models.FloatField(null=True, blank=True)
    when_made = models.DateField(blank=True, null=True)
    balance = models.FloatField(null=True, blank=True)
    depth = models.FloatField(null=True, blank=True)


class SchoolFeePayment(models.Model):
    student = models.ForeignKey(
        StudentExtra, null=True, on_delete=models.SET_NULL)
    schoolfees = models.FloatField(null=True)
    when_made = models.DateField(blank=True, null=True)
    debth = models.FloatField(null=True, blank=True)
    troll = models.BooleanField(default=False)
    soap = models.BooleanField(default=False)
    broom = models.BooleanField(default=False)


class Notice(models.Model):
    date = models.DateField(auto_now=True)
    by = models.CharField(max_length=20, null=True, default='school')
    message = models.CharField(max_length=500)


# ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
# source /var/home/monalksi2/virtualenv/src/3.7/bin/activate && cd /var/home/monalksi2/src
