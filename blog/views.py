from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Category, Post, Tag

# Create your views here.
def single(request):
	return render(request, 'single.html')

def get_category(request, slug):
	category = Category.objects.all()
	return render(request, 'category.html', {
		'category': category,
	})


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