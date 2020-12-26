from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect,redirect
from .models import Student,About,Teacher,Period,Student_Attendance_Information
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from location_field.models.plain import PlainLocationField

def index(request):
	obj= Student.objects.all()
	# tea_obj=Teacher.objects.all()
	# data_tea=''
	data=''
	if request.method == 'POST':
		standard=request.POST['std']
		roll= int(request.POST['rollno'])
		(standard)
		(roll)
		
	
		for i in obj:
			(i)
			stand=str(i.standard)
			roll_no=int(i.roll)
			# ('st',stand)
			# ('roll',roll_no)
			if standard==stand and roll==roll_no:
				data=i
			else:
				res = 'No Record Found...'
		return render(request,'blog/index.html',{'data':data,'res':res})
	return render(request,'blog/index.html')

def insert(request):
	
	if request.method=="POST":
		roll=request.POST['rollno']
		name=request.POST['name']
		city=request.POST['city']
		contact=request.POST['contact']
		std=request.POST['std']
		img=request.POST['img'].file.read()
		(roll,name,city,contact,std,img)
		
		s=Student(roll=roll,name=name,city=city,contact=contact,standard=std,image=img)
		s.save()
		(s)
		return render(request,'blog/insert.html')

	else:
		return render(request,'blog/insert.html')





def update(request):
	obj= Student.objects.all()
	
	obj=Student.objects.order_by().values('standard').distinct()
	if request.method == 'POST':
		data=[]
		s=1
		standard=request.POST['std']
		name= request.POST['stdname']
		stu=Student.objects.filter(standard=standard)
		for i in stu:
			if name in i.name:
				data.append((s,i))
				s+=1
		return render(request,'blog/update.html',{'data':data})
	return render(request,'blog/update.html',{'obj':obj})

def delete(request):
	obj= Student.objects.all()
	obj=Student.objects.order_by().values('standard').distinct()
	if request.method == 'POST':
		data=''
		standard=request.POST['std']
		name= request.POST['stdname']
		stu=Student.objects.filter(standard=standard,name=name)
		if stu.exists():
			data=stu.first()
		else:
			HttpResponse("<h1>Data not found</h1>")
		return render(request,'blog/delete.html',{'data':data})
	return render(request,'blog/delete.html')

def about(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		enquiry=request.POST['enquiry']
		phone=request.POST['phone']
		message=request.POST['message']

		user=About.objects.create(name=name,email=email,enquiry=enquiry,phone=phone,message=message)
		user.save()
		('User created')
		return redirect('/')
	return render(request,'blog/about.html')

def service(request):
	return render(request,'blog/service.html')

def contact(request):
	return render(request,'blog/contact.html')

def feedback(request):


		return render(request,'blog/feedback.html')



def register(request):
	if request.method=='POST':
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,'Username Already Exists !')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,'Email Already Exists !')
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
				user.save()
				('User created')
				return redirect('login')
		else:
			messages.info(request,'Password does not match !')
			return redirect('register')

	else:
		return render(request,'blog/register.html')

def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/')
		else:
			messages.info(request,'Invalid Username / Password !')
			return redirect('login')
	else:
		return render(request,'blog/login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

def dashboard(request):
	return render(request,'blog/dashboard.html')

@csrf_exempt
def teacher(request):
	tacher_obj=None
	if request.method=="POST":
		tea_emp_no=request.POST.get('empno')
		tea_phone_no=request.POST.get('phoneno')
		
		try:
		 tacher_obj=Teacher.objects.values().get(EmployeeNo=int(tea_emp_no),phoneNo=str(tea_phone_no))
		 period_obj=Period.objects.values().get(asgin_teacher=tacher_obj['id'])
		 return JsonResponse({'status':'Save','tacher_obj':tacher_obj,'period_obj':period_obj})
		 print(tacher_obj.id)
		except:
			print("data")
			return JsonResponse({'status':0})
		
		
	else:
		print('gate request is running')	
	return render(request,'blog/teachers.html',{'tacher_obj':tacher_obj})
	



def teacherAttandance(request,subid=None,studentid=None,periodname=None):
	student_present=request.GET.get("present")
	student_absent=request.GET.get("absent")
	if student_present==None:
		student_present=True
		student_absent=False
	else:
		pass


	period_obj=Period.objects.get(name=periodname)
	
	p = period_obj.student_name.all()
	context={'period_obj':period_obj,'p':p}
	return render(request,'blog/attandance.html',context)


@csrf_exempt
def succesws(request,subid,studentid,value):
	p=	Period.objects.get(id=subid)
	
	student_obj=Student.objects.get(id=studentid)
	if request.method=="POST":
		print(subid,studentid,value)
		print("post requestis running")
		sai=Student_Attendance_Information(
			student_name=student_obj,
			present=value,
			subject=p
		)
		sai.save()
	else:
		print("get request is running")	
	return redirect(f'/attandance/{p.name}')	

