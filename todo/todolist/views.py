from django.contrib import messages
from django.shortcuts import render,redirect
from .models import todo,users, emails_sub,contact_page_model
from .forms import contact_form, UserForm
from django.views import View
from django.views.generic import TemplateView,View
from django.contrib.auth import (authenticate,login,password_validation)
from django.contrib.auth.models import User

def index(request):
	if request.method=="POST":
		email = request.POST['email']
		subscriber = emails_sub(email=email)
		subscriber.save()
		messages.success (request,'Thanks for subscribing')
		return redirect('/')
	else:
		todos = todo.objects.all()
		user = users.objects.all()
		context = {
		'todos':todos,
		'user':user
		}
		return render(request,"index.html", context)

def todo_individual(request,id):
	listtodo = todo.objects.get(id=id)
	context={
	'listtodo':listtodo
	}
	return render(request,'todo.html',context)

def todos(request):
	todolist = todo.objects.all()
	context={
	'todolist':todolist
	}
	return render(request,'todos.html',context)

def add(request):
	if(request.method=='POST'):
		title = request.POST['title']
		text = request.POST['text']
		todos = todo(name=title,description=text)
		todos.save()
		messages.success(request,"Succesfully added note")
		return redirect('/')
	else:
		return render(request,'add.html')

def contact(request):
	if request.method=='POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		contact_info = contact_page_model(name=name,email=email,phone=phone,message=message)
		contact_info.save()
		messages.success(request,'Thanks for contacting us')
		return redirect('/contact')
	
	return render(request,'contact.html')

class ContactView(TemplateView):
	def get(self, request,*args,**kwargs):
		return render(request,'contact.html')
	def post(self, request,*args,**kwargs):
		form = contact_form(request.POST)
		if form.is_valid():
			name = request.POST['name']
			email = request.POST['email']
			phone = request.POST['phone']
			message = request.POST['message']
			contact_info = contact_page_model(name=name,email=email,phone=phone,message=message)
			contact_info.save()
			messages.success(request,'Thanks for contacting us')
		else:
			messages.error(request,'Error occured')
		return render(request,'contact.html')

class UserRegisterView(View):
	form_class = UserForm
	template_name = 'registration-form.html'

	#display a blank form and the user has no account
	def get(self,request):
		forma = self.form_class(None)
		return render(request,self.template_name,{'form':forma})

	#process for data and register users
	def post(self,request):
		forma = self.form_class(request.POST)

		if forma.is_valid():
			user = forma.save(commit=False)

			#cleaned and normalized data
			username=forma.cleaned_data['username']
			print(username)
			password=forma.cleaned_data['password']
			print(password)
			#user = set_password('new password')
			user.save()

			user.authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect('/')
		
		return render(request,self.template_name,{'form':forma})

class UserLoginView(View):
	form_class = UserForm

	def get(self,request):
		form = self.form_class(request.POST)
		return render(request,'login.html',{'form':form})
	def post(self,request):
		return render(request,'profile.html')


class UserProfileView(View):
	def get(self,request):
		pass
	def post(self,request):
		pass

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.success(request,'Succesfully loged out')
    return redirect('/')





