from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from dashboard.models import Posts
from django.template import RequestContext
from django.template.loader import render_to_string

# Create your views here.

def login(request):
	return render(request, 'dashboard/login.html')

def home(request):
	d = {}
	for obj in Posts.objects.all():
		temp = []
		temp = [obj.name, obj.description, obj.url, obj.datetime]
		d[obj.id] = temp
	return render(request,'dashboard/home.html', {'list' : d})

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