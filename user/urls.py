from django.urls import path

from .views import user_sign_up, user_sign_in, user_logout

urlpatterns = [
	path('sign_up', user_sign_up, name='sign_up'),
	path('sign_in', user_sign_in, name='sign_in'),
	path('logot', user_logout, name='logout'),
]
