from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from . models import Post, Post1, Editorial


#post
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
	return render(request, 'news/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'news/post_detail.html', {'post':post})
    
#post1    
def post1_list(request, pk):
    post1 = Post1.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[:3]
    return render(request, 'news/post1_list.html', {'posts1':posts1})

def post1_detail(request, pk):
	post1 = get_object_or_404(Post1, pk1=pk1)
	return render(request, 'news/post1_detail.html', {'post1':post1})

#editorial	
def editorial_list(request, pk):
	editorial = Editorial.objects.filter(edit_published_date__lte=timezone.now()).order_by('-edit_published_date')[:3]
	return render(request, 'news/editorial_list.html', {'editorials':editorials})