from django.db import models
# from location_field.models.plain import PlainLocationField
 

standard = (
    ('1st','1st'),
    ('2nd','2nd'),
    ('3rd','3rd'),
    ('4th','4th'),
    ('5th','5th'),
    ('6th','6th'),
    ('7th','7th'),
    ('8th','8th'),
    ('9th','9th'),
    ('10th','10th'),
    ('11th','11th'),
    ('12th','12th'),
    ('Diploma','Diploma'),
    ('Graduate','Graduate'),
    ('Post Graduate','Post Graduate'),
    ('PhD','PhD'),
    ('Others','Others'),
)

class Student(models.Model):
    # id = models.AutoField()
	roll = models.IntegerField()
	name = models.CharField(max_length=30)
	city = models.CharField(max_length=20)
	contact = models.CharField(max_length=20)
	standard = models.CharField(max_length=20,choices=standard,default='1st')
	image = models.ImageField(upload_to='images/')
    

	def __str__(self):
		return self.name


class About(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    enquiry = models.CharField(max_length=50)
    phone = models.IntegerField()
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    message = models.TextField(max_length=200)
    # maps = models.PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
        return self.name





class Feedback(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    organization = models.TextField(max_length=200)
    message = models.TextField(max_length=300)


    def __str__(self):
        return self.fname


class Teacher(models.Model):
    
	EmployeeNo = models.IntegerField(unique=True)
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=20)
	phoneNo = models.CharField(max_length=20,unique=True)
	degree = models.CharField(max_length=255)
	
	image = models.ImageField(upload_to='teachers/')
    

	def __str__(self):
		return self.name

class Period(models.Model):
    name = models.CharField(max_length=30)
    asgin_teacher=models.OneToOneField(Teacher,on_delete=models.CASCADE)
    student_name=models.ManyToManyField(Student)
    @staticmethod
    def all_period_student_id(period_id):
        if period_id:
            return Period.objects.filter(Period=period_id)
        else:
            return None    
    
    def student_involbed(self):
        string=','.join(str(p) for p in self.student_name.all())

        converting_list=list(string.split(","))
        return converting_list
    




    def __str__(self):
        return self.name



class Student_Attendance_Information(models.Model):
    # student_name=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='name')
    student_name=models.ForeignKey(Student,on_delete=models.CASCADE)
    # student_name=models.CharField(max_length=255)
    
    present=models.BooleanField()
    subject=models.ForeignKey(Period,on_delete=models.CASCADE)
    
    
    
    
	