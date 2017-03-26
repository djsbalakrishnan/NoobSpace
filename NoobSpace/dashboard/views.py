from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from dashboard.models import Posts
from django.template import RequestContext

# Create your views here.
def home(request):
	d = {}
	for obj in Posts.objects.all():
		temp = []
		temp = [obj.name, obj.description, obj.url, obj.datetime]
		d[obj.id] = temp
	return render(request,'dashboard/home.html', {'list' : d})