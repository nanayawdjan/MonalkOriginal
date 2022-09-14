from django.contrib import admin
from .models import StudentExtra,TeacherExtra,Notice,Payment,SchoolFeePayment
# Register your models here. (by sumit.luv)
class StudentExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudentExtra, StudentExtraAdmin)

class TeacherExtraAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherExtra, TeacherExtraAdmin)

class NoticeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Notice, NoticeAdmin)

class PaymentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Payment, PaymentAdmin)

class SchoolFeePaymentAdmin(admin.ModelAdmin):
    pass
admin.site.register(SchoolFeePayment, SchoolFeePaymentAdmin)
