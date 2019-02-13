from django.urls import path,re_path,include
from . import views

app_name='subscribe'
urlpatterns=[
	
	path("",views.subscribe_email,name='subscribe_email'),
]