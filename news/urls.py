from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('', views.post1_list, name='post1_list'),
	path('post1/<int:pk1>/', views.post1_detail, name='post1_detail'),
	#path('', views.editorial_list, name='editorial_list'),
]
