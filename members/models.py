from django.db import models

# class members(models.Model):
#   first_name = models.CharField(max_length=12)
#   last_name = models.CharField(max_length=12)
#   age = models.IntegerField()
#   email = models.CharField(max_length=20)
#   phone_number = models.IntegerField()
#   about = models.TextField()
#   date_of_birth = models.DateField()

#   def _str_(self):
#     return f"{self.first_name} {self.last_name} {self.age} {self.email} {self.phone_number} {self.about} {self.date_of_birth}"

# class Course(models.Model):
#   name = models.CharField(max_length=20)
#   code = models.CharField(max_length=20)
#   credit_unit= models.IntegerField()
#   course_coordinator = models.CharField(max_length=20 ,null=True)
# #   Course_ordinator = models.IntegerField()

#   def _str_(self):
#     return f"{self.name} {self.code} {self.credit_unit} {self.course_coordinator}"

# class student(models.Model):
#   first_name = models.CharField(max_length=20)
#   surname= models.CharField(max_length=20)
#   registration_number = models.CharField(max_length=20)
#   registration_course = models.CharField(max_length=20)
#   entry_fee= models.IntegerField()
#   current_semester = models.IntegerField()
#   age = models.IntegerField()
#   date_of_birth = models.DateField()
#   courses = models.ManyToManyField(Course,related_name= "student")
#   def _str_(self):
#     return f"{self.first_name} {self.surname} {self.registtration_number} {self.registtration_course} {self.entry_fee} {self.current_semester} {self.age} {self.date_of_birth}"

#   def course_list(self):
#     return ",".join([course.name for course in self.courses.all()])
#   course_list.short_description = 'Course'



# class Grades(models.Model):
#   student = models.CharField(max_length=20)
#   course = models.CharField(max_length=20)
#   ca = models .IntegerField()
#   exams = models.IntegerField()
#   total = models.IntegerField()
#   Grade = models.ManyToManyField(student, related_name="Grade")

#   def __str__(self):
#     return f"{self.student} {self.course} {self.ca } {self.exams } {self.total} "
  
  
# #   def adding_sum():
# #     return 

class Member(models.Model):
    firstname= models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone = models.IntegerField()
    joined_date = models.DateField()


def __str__(self):
     return f"{self.firstname} {self.lastname } {self.phone} {self.joined_date } "  

# class Home(models.Model):
#     firstname= models.CharField(max_length=30)
#     lastname = models.CharField(max_length=30)
#     phone = models.IntegerField()
#     joined_date = models.DateField()


# def __str__(self):
#      return f"{self.firstname} {self.lastname } {self.phone} {self.joined_date } "







# # Create your models here.