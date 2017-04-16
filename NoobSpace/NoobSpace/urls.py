from django.conf.urls import url
from django.contrib import admin
from dashboard import views

urlpatterns = [
	url(r'^$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
	url(r'^search/$', views.search, name='search'),
    url(r'^admin/', admin.site.urls),
]
