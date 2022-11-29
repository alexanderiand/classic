from django.db import models
from django.contrib.auth.models import User as BaseUser

from blog.models import Post

# Create your models here.
"""
	User
	-------------------
	id, name, email, password, photo
"""
class BlogUser(BaseUser):
	username = BaseUser.username
	email = BaseUser.email
	password = BaseUser.password
	photo = models.ImageField(upload_to='user/%Y/%m/%d', blank=True, null=True)

	class Meta:
		verbose_name = 'Пользователь'
		verbose_name_plural = 'Пользователи'
		ordering = ('username',)

	def __str__(self):
		return f'{self.username}'


"""
	Comment
	----------------------
	id, text, user_id (fk to user_id), post_id (fk to post_id), create_at
"""
class Comment(models.Model):
	user_id = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
	post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
	text = models.CharField(max_length=300, blank=True, verbose_name='Текст комментария')
	create_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'комментарии'
		ordering = ('create_at',)

	def __str__(self):
		return f'{self.text}'
