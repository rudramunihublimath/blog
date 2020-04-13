from django.forms import ModelForm
from .models import PetModel




class PetSearchForm(ModelForm):
	class Meta:
		model = PetModel
		fields = '__all__'