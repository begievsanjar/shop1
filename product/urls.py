from django.urls import path
from product.views import ShopListView

app_name = 'product'

urlpatterns = [
    path('shop/', ShopListView.as_view(), name='shop')
]
