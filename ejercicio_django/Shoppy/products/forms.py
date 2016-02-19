from django import forms
from .models import Product

#formulario de la clase Product
class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = '__all__'