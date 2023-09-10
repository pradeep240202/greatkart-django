from django.urls import path
# from .views import store
from .views import Store,ProductDetail

urlpatterns = [
    # path("",store,name="store"),
    path("",Store.as_view(),name='store'),
    path("<slug:product_slug>",ProductDetail.as_view(),name="product_detail"),
    # path("<slug:category_slug>",Store.as_view(),name="products_by_category"),
]
