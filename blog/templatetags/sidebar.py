from django import template

from ..models import Post

register = template.Library()

@register.inclusion_tag('sidebar_tpl.html')
def get_popular_post(count: int = 1) -> dict:
	""" get popular post by post views
	:param count: int  - post count
	:return dict: popular post
	"""
	posts = Post.objects.order_by('-view')[:count]
	return {'posts': posts}

@register.inclusion_tag('sidebar_tpl.html')
def get_recent_post(count: int = 3) -> dict:
	""" getting recent post """
	posts = Post.objects.order_by('-create_at')[:count]
	return {'posts': posts}