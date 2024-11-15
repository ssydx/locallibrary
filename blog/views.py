# 载入模型
from .models import *

# 视图函数
from django.shortcuts import render
def index(request):
    auth_num = BlogAuthorModel.objects.count()
    blog_num = BlogContentModel.objects.count()
    comment_num = BlogCommentModel.objects.count()
    return render(
        request,
        'blog/index.html',
        context= {
            'auth_num':auth_num,
            'blog_num':blog_num,
            'comment_num':comment_num,
        }
    )

# 视图
from django.views.generic import *
class BlogAuthorsView(ListView):
    model = BlogAuthorModel
    template_name = 'blog/authors.html'
    context_object_name = 'blogauthors'
class BlogContentsView(ListView):
    model = BlogContentModel
    template_name = 'blog/contents.html'
    context_object_name = 'blogcontents'
class BlogAuthorView(DetailView):
    model = BlogAuthorModel
    template_name = 'blog/author.html'
    context_object_name = 'blogauthor'
class BlogContentView(DetailView):
    model = BlogContentModel
    template_name = 'blog/content.html'
    context_object_name = 'blogcontent'