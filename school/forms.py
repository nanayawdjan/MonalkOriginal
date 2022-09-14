from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.models import User
from . import models
import datetime


class AllLogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

# for admin


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


# for student related form
class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name',
                  'username', 'password']


class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = models.StudentExtra
        fields = ['roll', 'cl', 'mobile', 'fee', 'status',
                  'date_of_admission', 'date_of_birth', 'gender', 'mother', 'father',
                  'residence', 'foodfee', 'carfee', 'passport']


# for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model = models.TeacherExtra
        fields = ['salary', 'mobile', 'status', 'passport']


# for notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model = models.Notice
        fields = '__all__'


# for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(
        max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class PaymentForm(forms.ModelForm):
    when_made = forms.DateField(initial=datetime.date.today)
    pay = forms.FloatField(initial=2)
    carpay = forms.FloatField(initial=4)

    class Meta:
        model = models.Payment
        fields = ['student', 'pay', 'carpay', 'schoolfees',
                  'balance', 'depth', 'when_made']


class SchoolFeePaymentForm(forms.ModelForm):
    when_made = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = models.SchoolFeePayment
        fields = ['student', 'schoolfees', 'when_made',
                  'debth', 'troll', 'soap', 'broom']

        # class Meta:
        # 	model = models.Payment
        # 	fields = ['student','pay','balance','depth','when_made']
    # when_made = forms.DateField(initial=datetime.date.today)
