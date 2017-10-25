from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from comments.forms import CommentForm
from .models import Post, Category


# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    category_list = Category.objects.all()
    context = {'post_list': post_list,
               'category_list': category_list
               }
    return render(request, 'blog/index.html', context=context)

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()

    form = CommentForm()
    comment_list = post.comment_set.all()

    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/post.html', context=context)