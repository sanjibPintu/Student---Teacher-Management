from django.contrib import admin
from .models import Student,About,Contact,Feedback,Teacher,Period,Student_Attendance_Information
from django.contrib.auth.models import Group

admin.site.site_header='HoD Admin InterFace'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name']
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Teacher)


# admin.site.unregister(Group)
@admin.register(Period)
class PeriodAdmin(admin.ModelAdmin):
    list_display=['id','name','asgin_teacher','student_involbed']


@admin.register(Student_Attendance_Information)
class Student_Attendance_InformationAdmin(admin.ModelAdmin):
    list_display=['student_name','present','subject']