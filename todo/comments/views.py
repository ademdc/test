from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import TemplateView,View
from django.contrib.auth import (authenticate,login,logout)
from .forms import UserForm
from django.contrib.auth.models import User

def index(request):
	return render(request,'index.html',{})

class CommentsView(TemplateView):
	template_name='comments.html'

class CommentsFormView(TemplateView):
	template_name='comments_form.html'

class RegisterUserView(View):
	template_name='register.html'
	form_class = UserForm
	def get(self,request):
		form = self.form_class(None)
		context={
		'form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST)
		context={
		'form':form
		}
		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			messages.success(request,"Successfully created user!")
			return redirect('/')

			if user is not None:
				if user.is_active:
					login(request,user)
					messages.success(request,"Successfully logged in!")
					return redirect('/')
			else:
				messages.error(request,"User is none")
				return redirect('/')
		else:
			messages.error(request,'Error occured while adding user')
			redirect(request,'/')

class LoginUserView(View):
	template_name='login.html'
	form_class = UserForm

	def get(self,request):
		form = self.form_class(None)
		context={
		'form':form
		}
		return render(request,self.template_name,context)

	def post(self,request):
		form = self.form_class(request.POST)
		context={
		'form':form
		}
		#if form.is_valid():
		username = request.POST['username'] #form.cleaned_data['username']
		print(username)
		password = request.POST['password']#form.cleaned_data['password']
		print(password)
		user = authenticate(username=username,password=password)

		if user is not None:
			if user.is_active:
				login(request,user)
				messages.success(request,'Logged in succesfully')
				return redirect('/comments/profile')
		else:
			messages.error(request,'Could not verify user')
			return render(request,self.template_name,context)

class LogoutUserView(View):
	def get(self,request):
	    logout(request)
	    messages.success(request,'Succesfully loged out')
	    return redirect('/comments/login')

class ProfileUserView(View):
	template_name='profile.html'
	def get(self,request):
	    return render(request,self.template_name,{'user':request.user})


