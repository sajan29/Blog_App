from django.shortcuts import render
from .models import Emails
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Emails
from django.core.mail import send_mail

# Create your views here.
@require_POST
def subscribe_email(request):
	try:
		email=request.POST.get('usr')
		print(request.POST)
		if email:
			try:
				validate_email(email)
				subobj,created=Emails.objects.get_or_create(email=email)
				send_mail('Subscribed for RSS Feeds','Hello '+email+'.You have been subscribed for the RSS Feeds from Blog Application\n\nHappy Blogging!!!!\n\nWith Regards,\nAdmin\n\nDont Reply to this system generated mail','sajanshaw8981@gmail.com',[email])
				if created:

					return JsonResponse({'status':'ok'})
				else:
					return JsonResponse({'status':'nok','message':'Already Subscribed'})
			except ValidationError:
				return JsonResponse({'status':'nok','message':'Not a valid email'})
		else:
			return JsonResponse({'status':'nok','message':'Some Error Occured'})
	except Exception as e:
		return JsonResponse({'status':'nok','message':e})





