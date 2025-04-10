from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import Post, Favorite

def index(request):
    return render(request, "blog/index.html")

def posts(request):
    posts = Post.objects.all()
    user_favorites = request.user.favorites.values_list('post_id', flat=True)

    for post in posts:
        post.is_favorited = post.id in user_favorites

    return render(request, "blog/posts.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})

def toggle_favorite(request, slug):
    post = get_object_or_404(Post, slug=slug)

    favorite = Favorite.objects.filter(user=request.user, post=post).first()
    
    if favorite:
        favorite.delete()
    else:
        f = Favorite.objects.create(user=request.user, post=post)
        f.save()
    
    return redirect('posts-blog')
