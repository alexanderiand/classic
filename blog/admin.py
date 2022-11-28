from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Tag, Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('id', 'title', 'slug', 'create_at')
	list_display_links = ('id', 'title', 'slug')
	search_fields = ('slug', 'title')
	list_filter = ('create_at',)
	save_as = True

class TagAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('id', 'title', 'slug')
	list_display_links = ('id', 'title')
	search_fields = ('title', 'slug')
	save_as = True

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('id', 'title', 'author', 'category', 'get_photo', 'create_at')
	list_display_links = ('id', 'title', 'author', 'category')
	search_fields = ('title', 'author', 'content')
	list_filter = ('create_at', 'author', 'view')
	list_per_page = 15
	list_max_show_all = 15
	save_as = True

	def get_photo(self, obj):
		if obj.photo:
			return mark_safe(f'<img src={obj.photo.url} width="80px" alt="post image" >')
		else:
			return 'фотография отсутствует'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
