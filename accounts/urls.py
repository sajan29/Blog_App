from django.urls import path,re_path,include
from . import views

app_name="accounts"

urlpatterns=[
	#Url for Sign Up
	re_path(r'^signup/$',views.signup,name='sign_up'),	
	#Url for Login
]