from django.urls import path
from main.views import HomeView, ContactView, AboutAsView

app_name = 'main'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about-as/', AboutAsView.as_view(), name='about-as')
]