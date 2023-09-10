from django.shortcuts import render
from store.models import Product
from django.views.generic import DetailView,ListView

# def home(request):
# 	return render(request,'home.html')


class Home(ListView):
	model = Product
	template_name = 'home.html'

	def get_queryset(self):
		return Product.objects.filter(is_available=True)