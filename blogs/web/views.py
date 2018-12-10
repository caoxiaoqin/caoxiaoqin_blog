from django.core.paginator import Paginator
from django.shortcuts import render

from user.models import Article


def index(request):
    """首页"""
    if request.method == 'GET':
        # 获取所有的文章
        article = Article.objects.all()
        page = request.GET.get('page', 1)
        # 分页 每页最多1条
        paginator = Paginator(article, 1)
        # 获取每一页的文章信息
        articles = paginator.page(page)
        return render(request, 'web/index.html', {'articles': articles})


def share(request):
    """相册"""
    if request.method == 'GET':
        return render(request, 'web/share.html')


def list(request):
    """列表"""
    if request.method == 'GET':
        return render(request, 'web/list.html')


def about(request):
    """关于"""
    if request.method == 'GET':
        return render(request, 'web/about.html')


def gbook(request):
    """"""
    if request.method == 'GET':
        return render(request, 'web/gbook.html')


def info(request):
    """文章内容"""
    if request.method == 'GET':

        # article = Article.objects.filter(pk=id).first()
        return render(request, 'web/info.html')


