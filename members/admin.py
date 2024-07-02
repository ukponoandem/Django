from django.contrib import admin
from .models import *


# # Register your models here.
# class MembersAdmin(admin.ModelAdmin):
#   list_display = ("first_name","last_name","age","email", "phone_number", "date_of_birth")
# admin.site.register(members, MembersAdmin)

# class CourseAdmin(admin.ModelAdmin):
#   list_display = ("name","code","credit_unit", "course_coordinator") 
# admin.site.register(Course, CourseAdmin)

# class studentsAdmin(admin.ModelAdmin):
#   list_display = ("first_name","surname","registration_number","registration_course", "entry_fee", "age", "course_list" ) 
# admin.site.register(student, studentsAdmin)


# class GradesAdmin(admin.ModelAdmin):
#   list_display = ("student","course","ca","exams", "total")
# admin.site.register(Grades, GradesAdmin)

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname","lastname","phone","joined_date")
admin.site.register(Member, MemberAdmin)