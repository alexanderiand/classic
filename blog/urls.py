from django.urls import path

from .views import single, get_category, MainView, CategoryView

urlpatterns = [
	path('', MainView.as_view(), name='main'),
	path('single/<str:slug>', single, name='view_post'),
	# path('category/<str:slug>', get_category, name='category')
	path('category/<str:slug>', CategoryView.as_view(), name='category')
]