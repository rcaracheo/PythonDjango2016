from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404

#modelos
from .models import Product
from . forms import ProductForm

def hello_world(request):
	product = Product.objects.order_by('id')
	template = loader.get_template('index.html')
	context = {
		'product': product
	}
	return HttpResponse(template.render(context, request))
	#return render(request, 'index.html')

def product_detail(request, pk):
	product = get_object_or_404(Product, pk=pk)
	template = loader.get_template('product_detail.html')
	context = {
		'product': product
	}

	return HttpResponse(template.render(context,request))

def new_product(request):
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		if form.is_valid():
			product = form.save()
			product.save()
			return HttpResponseRedirect('/')
	else:
		form = ProductForm()

	template = loader.get_template('new_product.html')
	context = {
		'form': form
	}

	return HttpResponse(template.render(context, request))