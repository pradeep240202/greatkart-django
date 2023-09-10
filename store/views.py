import django_filters
from django.shortcuts import render
from django.views.generic import DetailView,ListView
from store.models import Product
from django.shortcuts import get_object_or_404
from category.models import Category
# Create your views here.

# def store(request):
# 	return render(request,'store/store.html')

class ProductFilter(django_filters.FilterSet):
	category = django_filters.CharFilter(field_name='category__slug')

	class Meta:
		model = Product
		fields = ['category']

class Store(ListView):
	model = Product
	template_name = 'store/store.html'

	def get_queryset(self):
		queryset = Product.objects.filter(is_available=True)
		profile_filter = ProductFilter(self.request.GET,queryset=queryset)
		return profile_filter.qs

class ProductDetail(DetailView):
	model = Product
	template_name = 'store/product_detail.html'
	slug_field = 'product_slug'

	def get_object(self,queryset=None):
		# category = get_object_or_404(Category,slug=self.kwargs["category_slug"])
		product = get_object_or_404(Product,slug=self.kwargs["product_slug"])
		return product
