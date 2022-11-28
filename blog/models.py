from django.db import models
from django.urls import reverse

# Create your models here.
"""
	Category
	--------------------------------
	id, title, slug, create_at
"""


class Category(models.Model):
	""" Category model"""
	title = models.CharField(max_length=150, verbose_name='Категория')
	slug = models.SlugField(unique=True, verbose_name='url', db_index=True, max_length=150)
	create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

	def __str__(self):
		return f'{self.title}'

	def get_absolute_url(self):
		return reverse('category', kwargs={'slug': self.slug})

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ('-title', 'create_at')


""" 
	Tag
	------------------
	id, title, slug
"""


class Tag(models.Model):
	title = models.CharField(max_length=50, default='tag')
	slug = models.SlugField(unique=True, max_length=50, verbose_name='url')

	def __str__(self):
		return f'{self.title}'

	def get_absolute_url(self):
		return reverse('posts_by_tag', kwargs={'slug': self.slug})

	class Meta:
		ordering = ('title',)


"""
	Post
	------------------
	id (pk), title, slug, content, photo, views, create_at, update_at, author
	- category - many to one rel. foreign key to Category (category_id)
	- tags many to many rel. with posts post_tags	
"""


class Post(models.Model):
	title = models.CharField(max_length=255, verbose_name='Заголовок')
	slug = models.SlugField(max_length=255, verbose_name='url', unique=True, db_index=True)
	author = models.CharField(max_length=150, blank=True, null=True, verbose_name='Автор')
	content = models.TextField(blank=True, verbose_name='Контент')
	photo = models.ImageField(upload_to='media/image_posts/%Y/%m/%d')
	view = models.IntegerField(default=0, verbose_name='Количество просмотров')
	create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
	update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
	category = models.ForeignKey(Category, verbose_name='Категория поста', on_delete=models.PROTECT,
	                             related_name='posts')
	tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

	def __str__(self):
		return f'{self.title}'

	def get_absolute_url(self):
		return reverse('view_post', kwargs={'slug': self.slug})

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'
		ordering = ('title', 'update_at', 'create_at')


