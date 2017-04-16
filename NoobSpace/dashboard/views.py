from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from dashboard.models import Posts
from dashboard.forms import Login, Register
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

def login(request):
	if request.method == "POST":
		csrfContext = RequestContext(request)
		form = Login(request.POST)
		if form.is_valid():
			uname = form.cleaned_data['username']
			pword = form.cleaned_data['password']
			user = authenticate(username = uname, password = pword)
			if user is not None:
				post_dictionary = {}
				for obj in Posts.objects.all():
					temp_fields = []
					temp_fields = [obj.name, obj.description, obj.url, obj.datetime]
					post_dictionary[obj.id] = temp_fields
				return render(request,'dashboard/home.html', {'list' : post_dictionary})
			else:
				#should print it in the userinterface than HttpResponse
				login_form = Login()
				register_form = Register()
				error_message = "The username or password is incorrect"
				return render(request, 'dashboard/login.html', {'lform':login_form, 'rform':register_form, 'login_error':error_message})
	else:	
		login_form = Login()
		register_form = Register()
	return render(request, 'dashboard/login.html', {'lform':login_form, 'rform':register_form})

def register(request):
	if request.method == "POST":
		csrfContext = RequestContext(request)
		form = Register(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			fname = form.cleaned_data['fname']
			lname = form.cleaned_data['lname']			
			password = form.cleaned_data['password']
			cpassword = form.cleaned_data['cpassword']
			if password == cpassword:
				user = User.objects.create_user(username, email, password)
				user.first_name = fname
				user.last_name = lname
				user.save()
				post_dictionary = {}
				for obj in Posts.objects.all():
					temp_fields = []
					temp_fields = [obj.name, obj.description, obj.url, obj.datetime]
					post_dictionary[obj.id] = temp_fields
				return render(request,'dashboard/home.html', {'list' : post_dictionary})
			else:
				#should print it in the userinterface than HttpResponse
				login_form = Login()
				register_form = Register()
				error_message = "The confirm password and the password doesn't match"
				return render(request, 'dashboard/login.html', {'lform':login_form, 'rform':register_form, 'login_error':error_message})
	else:
		return HttpResponse("WTF <br/>Please report it to the user")

def search(request):
	tag = request.GET.get('value')
	d = {}
	objs = Posts.objects.filter(tag__contains=tag)
	for obj in objs:
		temp = []
		temp = [obj.name, obj.description, obj.url, obj.datetime]
		d[obj.id] = temp
	if request.is_ajax():
		html = render_to_string('dashboard/search.html',{'list' : d})
		return HttpResponse(html)