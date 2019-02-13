from django.forms import ModelForm
from subscribe.models import Emails

class EmailsForm(ModelForm):
	class Meta:
		model=Emails
		exclude=()

