from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Category, Post, Tag

# Create your views here.

def index(request):
	return render(request, 'index.html')

def single(request):
	return render(request, 'single.html')

def get_category(request, slug):
	category = Category.objects.all()
	return render(request, 'category.html', {
		'category': category,
	})