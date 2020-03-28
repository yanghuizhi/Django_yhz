import markdown
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.

# 第一代
# def index(request):
#     # return HttpResponse("欢迎访问我的博客首页！")
#     return render(request, 'app_blog/index.html', context={
#         'title': '我的博客首页',
#         'welcome': '欢迎访问我的博客首页'
#     })


from django.shortcuts import render
from .models import Post

# 第二代
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'app_blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body)
    post.toc = md.toc

    return render(request, 'app_blog/detail.html', context={'post': post})
