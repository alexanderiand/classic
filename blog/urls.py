from django.urls import path

from .views import index, single, get_category

urlpatterns = [
	path('', index, name='main'),
	path('single/', single, name='single'),
	path('category/<str:slug>', get_category, name='category')
]