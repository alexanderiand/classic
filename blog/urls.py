from django.urls import path

from .views import index, single, get_category, MainView

urlpatterns = [
	# path('', index, name='main'),
	path('', MainView.as_view(), name='main'),
	path('single/<str:slug>', single, name='view_post'),
	path('category/<str:slug>', get_category, name='category')
]