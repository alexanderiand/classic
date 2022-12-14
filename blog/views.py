from django.db.models import F
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Category, Post, Tag

# Create your views here.
class MainView(ListView):
	model = Post
	template_name = 'index.html'
	allow_empty = False
	paginate_by = 3
	context_object_name = 'posts'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Classic blog site'
		context['latest_post'] = Post.objects.all().last()
		return context


class CategoryView(ListView):
	model = Category
	template_name = 'category.html'
	allow_empty = False
	paginate_by = 3
	context_object_name = 'posts'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		current_category = Category.objects.get(slug=self.kwargs['slug'])
		context['title'] = current_category.title
		context['posts'] = Post.objects.filter(category__slug=self.kwargs['slug'])
		context['latest_post'] = Post.objects.filter(category__slug=self.kwargs['slug']).last()
		return context


class PostView(DetailView):
	model = Post
	template_name = 'single.html'
	slug_url_kwarg = 'slug'
	context_object_name = 'post'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		self.object.views = F('view') + 1  # every time user view
		self.object.save()  # saves
		try:
			post = Post.objects.get(slug=self.kwargs['slug'])
		except Exception:
			raise Http404('Page not found!')

		context['post'] = post
		context['tags'] = post.tags.all()
		return context

class TagView(ListView):
	model = Tag
	template_name = 'tag.html'
	context_object_name = 'posts'
	allow_empty = False
	paginate_by = 1

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		tag = Tag.objects.get(slug=self.kwargs['slug'])
		context['title'] = f'Tag: {tag.title}'
		context['posts'] = Post.objects.filter(tags__slug=self.kwargs['slug'])
		return context


class SearchView(ListView):
	template_name = 'search.html'
	context_object_name = 'posts'

	def get_queryset(self):
		return Post.objects.filter(title__icontains=self.request.GET.get('s'))

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Search'
		return context
