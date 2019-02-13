
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .models import Post

# Create your views here
def post_list_view(request):
	list_objects=Post.published.all()
	paginator=Paginator(list_objects,2)
	page=request.GET.get('page')
	count=User.objects.count()
	try:
		posts=paginator.page(page)
	except PageNotAnInteger:
		posts=paginator.page(1)
	except EmptyPage:
		posts=paginator.page(paginator.num_pages)
		


	return render(request,'blog/post/list.html',{'posts':posts,'count':count})

def post_detail_view(request,year,month,day,post):
	post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
	return render(request,'blog/post/detail.html',{'post':post})	


 