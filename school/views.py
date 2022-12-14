from multiprocessing import context
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .import forms, models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from django.db.models import OuterRef, Subquery


# from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# ================================= LOGIN VIEW ================================ #
# ================================= LOGIN VIEW ================================ #
# ================================= LOGIN VIEW ================================ #
@unauthenticated_user
def all_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('')
    context = {}
    return render(request, 'school/others/login.html', context)

# ============================ END OF LOGIN VIEW ================================ #
# ============================ END OF LOGIN VIEW ================================ #
# ============================ END OF LOGIN VIEW ================================ #


def home_view(request):
    return render(request, 'school/others/index.html')


@unauthenticated_user
def clicked_signup_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'school/others/signup_option.html')


@unauthenticated_user
def student_signup_view(request):
    form1 = forms.StudentUserForm()
    form2 = forms.StudentExtraForm()
    mydict = {'form1': form1, 'form2': form2}
    if request.method == 'POST':
        form1 = forms.StudentUserForm(request.POST)
        form2 = forms.StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print('worked')
            user = form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.user = user
            user2 = f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
        else:
            print('not correct')

        return HttpResponseRedirect('login')
    return render(request, 'school/student/studentsignup.html', context=mydict)


@unauthenticated_user
def teacher_signup_view(request):
    form1 = forms.TeacherUserForm()
    form2 = forms.TeacherExtraForm()
    mydict = {'form1': form1, 'form2': form2}
    if request.method == 'POST':
        form1 = forms.TeacherUserForm(request.POST)
        form2 = forms.TeacherExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.user = user
            user2 = f2.save()

            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)

        return HttpResponseRedirect('teacherlogin')
    return render(request, 'school/teacher/teachersignup.html', context=mydict)


# for checking user is techer , student or admin
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()


def is_teacher(user):
    return user.groups.filter(name='TEACHER').exists()


def is_student(user):
    return user.groups.filter(name='STUDENT').exists()


def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_teacher(request.user):
        accountapproval = models.TeacherExtra.objects.all().filter(
            user_id=request.user.id, status=True)
        if accountapproval:
            return redirect('teacher-dashboard')
        else:
            return render(request, 'school/teacher/teacher_wait_for_approval.html')
    elif is_student(request.user):
        accountapproval = models.StudentExtra.objects.all().filter(
            user_id=request.user.id, status=True)
        if accountapproval:
            return redirect('student-dashboard')
        else:
            return render(request, 'school/student/student_wait_for_approval.html')


# for dashboard of adminnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_dashboard_view(request):
    teachercount = models.TeacherExtra.objects.all().filter(status=True).count()
    pendingteachercount = models.TeacherExtra.objects.all().filter(status=False).count()

    studentcount = models.StudentExtra.objects.all().filter(status=True).count()
    pendingstudentcount = models.StudentExtra.objects.all().filter(status=False).count()

    teachersalary = models.TeacherExtra.objects.filter(
        status=True).aggregate(Sum('salary'))
    pendingteachersalary = models.TeacherExtra.objects.filter(
        status=False).aggregate(Sum('salary'))

    studentfee = models.StudentExtra.objects.filter(
        status=True).aggregate(Sum('fee', default=0))
    pendingstudentfee = models.StudentExtra.objects.filter(
        status=False).aggregate(Sum('fee'))

    notice = models.Notice.objects.all()

    # aggregate function return dictionary so fetch data from dictionay
    mydict = {
        'teachercount': teachercount,
        'pendingteachercount': pendingteachercount,

        'studentcount': studentcount,
        'pendingstudentcount': pendingstudentcount,

        'teachersalary': teachersalary['salary__sum'],
        'pendingteachersalary': pendingteachersalary['salary__sum'],

        'studentfee': studentfee['fee__sum'],
        'pendingstudentfee': pendingstudentfee['fee__sum'],

        'notice': notice,

    }

    return render(request, 'school/admin/admin_dashboard.html', context=mydict)


# for teacher sectionnnnnnnn by adminnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_teacher_view(request):
    return render(request, 'school/admin/admin_teacher.html')


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_add_teacher_view(request):
    form1 = forms.TeacherUserForm()
    form2 = forms.TeacherExtraForm()
    mydict = {'form1': form1, 'form2': form2}
    if request.method == 'POST':
        form1 = forms.TeacherUserForm(request.POST)
        form2 = forms.TeacherExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()

            f2 = form2.save(commit=False)
            f2.user = user
            f2.status = True
            f2.save()

            my_teacher_group = Group.objects.get_or_create(name='TEACHER')
            my_teacher_group[0].user_set.add(user)

        return HttpResponseRedirect('admin-teacher')
    return render(request, 'school/admin/admin_add_teacher.html', context=mydict)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_view_teacher_view(request):
    teachers = models.TeacherExtra.objects.all().filter(status=True)
    return render(request, 'school/admin/admin_view_teacher.html', {'teachers': teachers})


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_approve_teacher_view(request):
    teachers = models.TeacherExtra.objects.all().filter(status=False)
    return render(request, 'school/admin/admin_approve_teacher.html', {'teachers': teachers})


@login_required(login_url='login')
@user_passes_test(is_admin)
def approve_teacher_view(request, pk):
    teacher = models.TeacherExtra.objects.get(id=pk)
    teacher.status = True
    teacher.save()
    return redirect(reverse('admin-approve-teacher'))


@login_required(login_url='login')
@user_passes_test(is_admin)
def delete_teacher_view(request, pk):
    teacher = models.TeacherExtra.objects.get(id=pk)
    user = models.User.objects.get(id=teacher.user_id)
    user.delete()
    teacher.delete()
    return redirect('admin-approve-teacher')


@login_required(login_url='login')
@user_passes_test(is_admin)
def delete_teacher_from_school_view(request, pk):
    teacher = models.TeacherExtra.objects.get(id=pk)
    user = models.User.objects.get(id=teacher.user_id)
    user.delete()
    teacher.delete()
    return redirect('admin-view-teacher')


@login_required(login_url='login')
@user_passes_test(is_admin)
def update_teacher_view(request, pk):
    teacher = models.TeacherExtra.objects.get(id=pk)
    user = models.User.objects.get(id=teacher.user_id)

    form1 = forms.TeacherUserForm(instance=user)
    form2 = forms.TeacherExtraForm(instance=teacher)
    mydict = {'form1': form1, 'form2': form2}

    if request.method == 'POST':
        form1 = forms.TeacherUserForm(request.POST, instance=user)
        form2 = forms.TeacherExtraForm(request.POST, instance=teacher)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.status = True
            f2.save()
            return redirect('admin-view-teacher')
    return render(request, 'school/admin/admin_update_teacher.html', context=mydict)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_view_teacher_salary_view(request):
    teachers = models.TeacherExtra.objects.all()
    return render(request, 'school/admin/admin_view_teacher_salary.html', {'teachers': teachers})


# for student by adminnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn

@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_student_view(request):
    return render(request, 'school/admin/admin_student.html')


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_add_student_view(request):
    form1 = forms.StudentUserForm()
    form2 = forms.StudentExtraForm()
    mydict = {'form1': form1, 'form2': form2}
    if request.method == 'POST':
        form1 = forms.StudentUserForm(request.POST)
        form2 = forms.StudentExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("form is valid")
            user = form1.save()
            user.set_password(user.password)
            user.save()

            f2 = form2.save(commit=False)
            f2.user = user
            f2.status = True
            f2.save()

            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)
            messages.success(request, 'Adding student was successful')
            return HttpResponseRedirect('admin-student')

        else:
            print("form is invalid")
            messages.error(request, 'Could not add student')
    return render(request, 'school/admin/admin_add_student.html', context=mydict)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_view_student_view(request):
    students = models.StudentExtra.objects.all().filter(status=True)
    return render(request, 'school/admin/admin_view_student.html', {'students': students})


@login_required(login_url='login')
@user_passes_test(is_admin)
def delete_student_view(request, pk):
    student = models.StudentExtra.objects.get(id=pk)
    user = models.User.objects.get(id=student.user_id)
    user.delete()
    student.delete()
    return redirect('admin-approve-student')


@login_required(login_url='login')
@user_passes_test(is_admin)
def update_student_view(request, pk):
    student = models.StudentExtra.objects.get(id=pk)
    user = models.User.objects.get(id=student.user_id)
    form1 = forms.StudentUserForm(instance=user)
    form2 = forms.StudentExtraForm(instance=student)
    mydict = {'form1': form1, 'form2': form2}
    if request.method == 'POST':
        form1 = forms.StudentUserForm(request.POST, instance=user)
        form2 = forms.StudentExtraForm(request.POST, instance=student)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            user.set_password(user.password)
            user.save()
            f2 = form2.save(commit=False)
            f2.status = True
            f2.save()
            return redirect('individual_student_info', pk)
    return render(request, 'school/admin/admin_update_student.html', context=mydict)


@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_approve_student_view(request):
    students = models.StudentExtra.objects.all().filter(status=False)
    return render(request, 'school/admin/admin_approve_student.html', {'students': students})


@login_required(login_url='login')
@user_passes_test(is_admin)
def approve_student_view(request, pk):
    students = models.StudentExtra.objects.get(id=pk)
    students.status = True
    students.save()
    return redirect(reverse('admin-approve-student'))


# notice related viewsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
@login_required(login_url='login')
@user_passes_test(is_admin)
def admin_notice_view(request):
    form = forms.NoticeForm()
    if request.method == 'POST':
        form = forms.NoticeForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.by = request.user.first_name
            form.save()
            return redirect('admin-dashboard')
    return render(request, 'school/admin/admin_notice.html', {'form': form})


# for TEACHER  LOGIN    SECTIONNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
@login_required(login_url='login')
@user_passes_test(is_admin)
def teacher_dashboard_view(request):
    teacherdata = models.TeacherExtra.objects.all().filter(
        status=True, user_id=request.user.id)
    notice = models.Notice.objects.all()
    mydict = {
        'salary': teacherdata[0].salary,
        'mobile': teacherdata[0].mobile,
        'date': teacherdata[0].joindate,
        'notice': notice
    }
    return render(request, 'school/teacher/teacher_dashboard.html', context=mydict)


@login_required(login_url='login')
@user_passes_test(is_admin)
def teacher_notice_view(request):
    form = forms.NoticeForm()
    if request.method == 'POST':
        form = forms.NoticeForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.by = request.user.first_name
            form.save()
            return redirect('teacher-dashboard')
        else:
            print('form invalid')
    return render(request, 'school/teacher/teacher_notice.html', {'form': form})


# FOR STUDENT AFTER THEIR Loginnnnnnnnnnnnnnnnnnnnn
@login_required(login_url='login')
def student_dashboard_view(request):
    studentdata = models.StudentExtra.objects.all().filter(
        status=True, user_id=request.user.id)
    notice = models.Notice.objects.all()
    context = {
        'roll': studentdata[0].roll,
        'gender': studentdata[0].gender,
        'mother': studentdata[0].mother,
        'father': studentdata[0].father,
        'residence': studentdata[0].residence,
        'date_of_birth': studentdata[0].date_of_birth,
        'date_of_admission': studentdata[0].date_of_admission,
        'cl': studentdata[0].cl,
        'notice': notice,
        'debt': studentdata[0].debt,
        'balance': studentdata[0].balance
    }
    return render(request, 'school/student/student_dashboard.html', context)


# for payment=========================================================================================


@login_required(login_url='login')
@user_passes_test(is_admin)
def individual_student_info_view(request, pk):
    student = models.StudentExtra.objects.get(id=pk)
    pay_record = student.payment_set.all()
    dcr = pay_record.aggregate(thepaid=Sum('pay'))
    dbr = pay_record.aggregate(dbrpay=Sum('carpay'))
    dtr = pay_record.aggregate(dtrpay=Sum('schoolfees'))
    bala = models.Payment.objects.all()

    # user = models.User.objects.get(id=student.user_id)
    if request.method == 'POST':
        student.status = False
        student.save()
        return redirect('admin-view-student')
    context = {
        'student': student,
        'pay_record': pay_record,
        'dcr': dcr,
        'dbr': dbr,
        'dtr': dtr,
        'bala': bala
    }
    return render(request, 'school/others/individual_student_info.html', context)

# I WILL COME BACK TO U


def delete_notice_view(request, pk):
    notice = models.Notice.objects.get(id=pk)
    notice.delete()
    return redirect('/')


# for aboutus and contact ussssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
def aboutus_view(request):
    return render(request, 'school/others/aboutus.html')


def sendEmail(request):
    if request.method == 'POST':
        template = render_to_string('school/others/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],
        })
        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['nanayawdjan446@gmail.com']
        )
        email.fail_silently = False
        email.send()
        print(template)
        messages.success(request, 'Reaching out to us was successful')
    return render(request, 'school/others/aboutus.html')


# @login_required(login_url='login')
# @user_passes_test(is_admin)
# def all_crucial_buttons_view(request):
#     context = {}
#     return render(request, 'school/admin/all_crucial_buttons.html', context)


# ================================= DAILY FEES PAYMENT ================================ #
# ================================= DAILY FEES PAYMENT ================================ #
# ================================= DAILY FEES PAYMENT ================================ #

@login_required(login_url='login')
@user_passes_test(is_admin)
def make_payment(request):
    students = models.StudentExtra.objects.all().filter(
        status=True, checkifpaiddaily=False)
    resetall = models.StudentExtra.objects.filter(checkifpaiddaily=True)
    if request.method == 'POST':
        resetall.update(checkifpaiddaily=False)
        return redirect('make-payment')
    context = {
        'students': students,
    }
    return render(request, 'school/admin/make_payment.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def day_pay_view(request, pk):
    student = models.StudentExtra.objects.get(id=pk)
    student_pay = student.payment_set.all()
    form2 = forms.PaymentForm(initial={'student': student})
    if request.method == 'POST':
        form2 = forms.PaymentForm(request.POST)
        if form2.is_valid():
            deb = form2.cleaned_data['depth']
            bala = form2.cleaned_data['balance']
            student.balance = bala
            student.debt = deb
            student.checkifpaiddaily = True
            student.save()
            form2.save()

        return redirect('make-payment')

    context = {
        'student': student,
        'form2': form2,
        'student_pay': student_pay,
    }
    return render(request, 'school/admin/payment.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def record_of_payment_view(request):
    record = models.Payment.objects.all()
    context = {'record': record}
    return render(request, 'school/admin/record_of_payment.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def deletepay_view(request, pk):
    payment = models.Payment.objects.get(id=pk)
    payment.delete()
    return redirect('record_of_payment')


@login_required(login_url='login')
@user_passes_test(is_admin)
def history_of_day_payment_view(request):
    dfmr = models.Payment.objects.filter().values('when_made').order_by(
        'when_made').annotate(sum=Sum('pay'), sum2=Sum('carpay'), sum3=Sum('schoolfees'))
    dsmr = models.SchoolFeePayment.objects.filter().values(
        'when_made').order_by('when_made').annotate(sum4=Sum('schoolfees'))
    context = {'dfmr': dfmr,
               'dsmr': dsmr,
               }
    return render(request, 'school/admin/history_of_day_pay.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def delete_individual_pay_view(request, pk):
    payment = models.Payment.objects.get(id=pk)
    payment.delete()

    return redirect('admin-view-student')


@login_required(login_url='login')
@user_passes_test(is_admin)
def reset_students_view(request):
    students = models.StudentExtra.objects.filter(checkifpaiddaily=True)
    context = {
        'students': students
    }
    return render(request, 'school/admin/reset_students_view.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def reset_single_payment(request, pk):
    reset_single = models.StudentExtra.objects.get(id=pk)
    reset_single.checkifpaiddaily = False
    reset_single.save()
    return redirect('make-payment')


# ================X================= END OF DAILY FEES PAYMENT ===============X================= #
# ================X================= END OF DAILY FEES PAYMENT ===============X================= #
# ================X================= END OF DAILY FEES PAYMENT ===============X================= #


# ================================= SCHOOL FEES PAYMENT ================================ #
# ================================= SCHOOL FEES PAYMENT ================================ #
# ================================= SCHOOL FEES PAYMENT ================================ #


@login_required(login_url='login')
@user_passes_test(is_admin)
def makeSchoolFeesPaymentView(request):
    students = models.StudentExtra.objects.filter(
        status=True, checkifpaidterm=False, payment_method='School_Fees_Aside')
    resetall = models.StudentExtra.objects.filter(checkifpaidterm=True)
    if request.method == 'POST':
        resetall.update(checkifpaidterm=False)
        students.update(debt=210)
        return redirect('school-fees-payment')
    context = {'students': students}
    return render(request, 'school/admin/make_schoolfees_payment.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def termPayView(request, pk):
    student = models.StudentExtra.objects.get(id=pk)
    form = forms.SchoolFeePaymentForm(initial={'student': student})
    student_pay = student.schoolfeepayment_set.all()
    addedup = student_pay.aggregate(thesum=Sum('schoolfees'))
    if request.method == 'POST':
        form = forms.SchoolFeePaymentForm(request.POST)
        if form.is_valid():
            deb = form.cleaned_data['debth']
            student.debt = deb
            if form.cleaned_data['debth'] == 0 and form.cleaned_data['troll'] == True and form.cleaned_data['soap'] == True and form.cleaned_data['broom'] == True:
                student.checkifpaidterm = True
            student.save()
            form.save()
        return redirect('school-fees-payment')
    context = {
        'student': student,
        'form': form,
        'student_pay': student_pay,
        'addedup': addedup,
    }
    return render(request, 'school/admin/term_pay.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def recordOfAllSchoolFeePayment(request):
    record = models.SchoolFeePayment.objects.all()
    context = {'record': record}
    return render(request, 'school/admin/record_of_all_school_fee_payment.html', context)


@login_required(login_url='login')
@user_passes_test(is_admin)
def deleteSchoolFeePayView(request, pk):
    payment = models.SchoolFeePayment.objects.get(id=pk)
    payment.delete()
    return redirect('record-of-all-school-fee-payment')


# ================================= END SCHOOL FEES PAYMENT ================================ #
# ================================= END SCHOOL FEES PAYMENT ================================ #
# ================================= END SCHOOL FEES PAYMENT ================================ #


# ================================= THOSE HAVING OUR MONEY ================================ #
# ================================= THOSE HAVING OUR MONEY ================================ #
# ================================= THOSE HAVING OUR MONEY ================================ #
@login_required(login_url='login')
@user_passes_test(is_admin)
def those_having_our_money(request):
    records = models.StudentExtra.objects.exclude(debt=0)
    print(records)

    context = {'records': records}
    return render(request, 'school/admin/those_owing.html', context)


# ================================= END OF THOSE HAVING OUR MONEY ================================ #
# ================================= END OF THOSE HAVING OUR MONEY ================================ #
# ================================= END OF THOSE HAVING OUR MONEY ================================ #
