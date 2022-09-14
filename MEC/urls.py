"""MEC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name=''),
    path('clicked_signup', views.clicked_signup_view, name='clicked_signup'),

    # ================================= ALL ABOUT AUTHENTICATION ================================ #
    # ================================= ALL ABOUT AUTHENTICATION ================================ #
    # ================================= ALL ABOUT AUTHENTICATION ================================ #
    path('studentsignup', views.student_signup_view, name='studentsignup'),
    path('teachersignup', views.teacher_signup_view, name="studentsignup"),
    path('login/', views.all_login, name="login"),
    # ================================= END ALL ABOUT AUTHENTICATION ================================ #
    # ================================= END ALL ABOUT AUTHENTICATION ================================ #
    # ================================= END ALL ABOUT AUTHENTICATION ================================ #

    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('logout', LogoutView.as_view(
        template_name='school/others/index.html'), name='logout'),


    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),


    # ADDED NOW
    path('admin-notice', views.admin_notice_view, name='admin-notice'),
    path('teacher-dashboard', views.teacher_dashboard_view,
         name='teacher-dashboard'),
    path('teacher-notice', views.teacher_notice_view, name='teacher-notice'),
    path('student-dashboard', views.student_dashboard_view,
         name='student-dashboard'),


    path('admin-teacher', views.admin_teacher_view, name='admin-teacher'),
    path('admin-add-teacher', views.admin_add_teacher_view,
         name='admin-add-teacher'),
    path('admin-view-teacher', views.admin_view_teacher_view,
         name='admin-view-teacher'),
    path('admin-approve-teacher', views.admin_approve_teacher_view,
         name='admin-approve-teacher'),
    path('approve-teacher/<int:pk>',
         views.approve_teacher_view, name='approve-teacher'),
    path('delete-teacher/<int:pk>',
         views.delete_teacher_view, name='delete-teacher'),
    path('delete-teacher-from-school/<int:pk>',
         views.delete_teacher_from_school_view, name='delete-teacher-from-school'),
    path('update-teacher/<int:pk>',
         views.update_teacher_view, name='update-teacher'),
    path('admin-view-teacher-salary', views.admin_view_teacher_salary_view,
         name='admin-view-teacher-salary'),


    path('admin-student', views.admin_student_view, name='admin-student'),
    path('admin-add-student', views.admin_add_student_view,
         name='admin-add-student'),
    path('admin-view-student', views.admin_view_student_view,
         name='admin-view-student'),
    path('delete-student-from-school/<int:pk>',
         views.delete_student_from_school_view, name='delete-student-from-school'),
    path('delete-student/<int:pk>',
         views.delete_student_view, name='delete-student'),
    path('update-student/<int:pk>',
         views.update_student_view, name='update-student'),
    path('admin-approve-student', views.admin_approve_student_view,
         name='admin-approve-student'),
    path('approve-student/<int:pk>',
         views.approve_student_view, name='approve-student'),


    path('std-payment/<str:pk>/', views.day_pay_view, name='admin-payment'),
    path('make-payment', views.make_payment, name='make-payment'),
    path('record_of_payment/', views.record_of_payment_view,
         name='record_of_payment'),
    path('history_of_day_payment/', views.history_of_day_payment_view,
         name='history_of_day_payment'),
    path('delete-payment/<int:pk>', views.deletepay_view, name='delete-payment'),
    path('delete-individual-pay/<str:pk>',
         views.delete_individual_pay_view, name='delete-individual-pay'),
    path('individual_student_info/<str:pk>/',
         views.individual_student_info_view, name='individual_student_info'),


    path('delete-notice/<str:pk>', views.delete_notice_view, name='delete-notice'),
    path('resetpayment/', views.reset_daily_payment_button, name='resetpayment'),
    path('resetsinglepayment/<int:pk>',
         views.reset_single_payment, name='resetsinglepayment'),
    path('reset_students_payment/',
         views.reset_students_view, name='reset_students'),
    path('all_crucial_buttons/', views.all_crucial_buttons_view,
         name='all_crucial_buttons'),


    # ====================================== SCHOOL FEES PAYMENT ===================================
    path('school-fees-payment/', views.makeSchoolFeesPaymentView,
         name='school-fees-payment'),
    path('term-pay-view/<str:pk>/', views.termPayView, name='term-pay-view'),
    path('record-of-all-school-fee-payment/', view=views.recordOfAllSchoolFeePayment,
         name='record-of-all-school-fee-payment'),
    path('delete-school-fee-pay/<int:pk>',
         views.deleteSchoolFeePayView, name='delete-school-fee-pay'),
    path('reset-term-schoolfees', views.reset_term_schoolfees,
         name='reset-term-schoolfees'),

    # ================================== END OF SCHOOL FEES PAYMENT ================================

    path('aboutus', views.aboutus_view, name='aboutus'),
    path('send_email/', views.sendEmail, name="send_email"),
    # path('contactus', views.contactus_view, name='contactus'),
]
