from django.urls import path,re_path,include
from . import views
from .feeds import PostsFeed

app_name = 'blog'

urlpatterns=[
	
	re_path(r'^$',views.post_list_view,name='post_list_view'),

	re_path(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',
		views.post_detail_view,name='post_detail_view'),

	re_path(r'^feed/$',PostsFeed(),name='post_feed'),

	# re_path(r'^accounts/signup/$',views.signup,name='sign_up'),

	# path('accounts/',include('django.contrib.auth.urls')),

]