from django.urls import path

from .views import MainView, CategoryView, PostView, TagView, SearchView

urlpatterns = [
	path('', MainView.as_view(), name='main'),
	path('category/<str:slug>', CategoryView.as_view(), name='category'),
	path('view_post/<str:slug>', PostView.as_view(), name='view_post'),
	path('posts_by_tag/<str:slug>', TagView.as_view(), name="posts_by_tag"),
	path('search/', SearchView.as_view(), name='search')
]