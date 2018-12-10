# encoding: utf-8
"""
@author: 曹晓芹


"""
from django.core.paginator import Paginator
from django.urls import reverse

from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from user.form import AddArticle
from user.models import UserName, Article, Prices


def register(request):
    """注册"""
    if request.method == 'GET':
        return render(request, 'user/register.html')
    if request.method == 'POST':
        # 1 获取用户
        name = request.POST.get('name')
        # 2 获取密码
        password = request.POST.get('password')
        # 加密密码
        password = make_password(password)

        # 3 验证数据的完整性
        if not all([name, password]):
            msg = '请填写完整的信息'
            return render(request, 'user/register.html', {'msg': msg})
        # 4 验证用户是否在数据库中存在 （验证用户是否被注册）
        if UserName.objects.filter(username=name).first():
            msg = '账号已经被注册'
            return render(request, 'login.html', {'msg': msg})
        # 创建数据
        UserName.objects.create(username=name,
                                password=password)
        return HttpResponseRedirect('user/login/')


def login(request):
    """登录"""
    if request.method == 'GET':
        return render(request, 'user/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        userpwd = request.POST.get('userpwd')
        # 1. 验证数据的完整性
        if not all(['name', 'userpwd']):
            msg = '请填写完整的信息'
            return render(request, 'user/login.html', {'msg': msg})
        # 2. 验证用户是否被注册过
        user = UserName.objects.filter(username=username).first()
        # 如果有用户 就说明有被注册过
        if user:
            # 3.解密
            # 验证密码是否正确
            if check_password(userpwd, user.password):
                # 4. 把user_id存到session中
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('user:index'))
            else:
                msg = '密码不正确'
                return render(request, 'user/login.html', {'msg': msg})
        else:
            msg = ''
            return render(request, 'user/login.html', {'msg': msg})


def index(request):
    """首页"""
    if request.method == 'GET':
        return render(request, 'user/index.html')


def article(request):
    """文章"""
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        # 查询所有文章 并进行分页
        articles = Article.objects.all()
        # 将所有文章进行分页 每页最 多1条数据
        paginator = Paginator(articles, 1)
        # 获取那一页的文章信息（这里拿的第一页）
        arts = paginator.page(page)
        return render(request, 'user/article.html', {'arts': arts})


def add_article(request):
    """添加文章"""
    if request.method == 'GET':
        return render(request, 'user/add-article.html')
    if request.method == 'POST':
        # 把from表单的数据提交给form验证
        # form = AddArticle(request.POST, request.FILES)
        user = request.user
        form = AddArticle(request.POST)
        # 1 验证成功就返回true
        if form.is_valid():
            # 2 那么创建数据 存储到数据库中
            Article.objects.create(title=form.cleaned_data.get('title'),
                                   describe=form.cleaned_data.get('describe'),
                                   content=form.cleaned_data.get('content'),
                                   tags=form.cleaned_data.get('tags'),
                                   keywords=form.cleaned_data.get('keywords'),
                                   art_user_id=user.id)

            # 添加成功就返回文章页面
            return HttpResponseRedirect(reverse('user:article'))
        # 没有提交成功 就返回添加文章页面
        error = form.errors
        return render(request, 'user/add-article.html', {'error': error})


def del_article(request, id):
    """delete article"""
    if request.method == 'GET':
        # 思路是 ：获取文章id 再删除文章
        # id = request.GET.get('id')
        # 查询到文章id之后再删除
        Article.objects.filter(pk=id).delete()
        return HttpResponseRedirect(reverse('user:article'))


def update_article(request, id):
    """更新数据"""
    if request.method == 'GET':
        # 获取pk=id的文章
        article = Article.objects.filter(pk=id).first()
        return render(request, 'user/update-article.html', {'article': article})
    if request.method == 'POST':
        # form = AddArticle(request.POST, request.FILES)
        form = AddArticle(request.POST)
        if form.is_valid():
            # 验证成功
            # titlepic = form.cleaned_data.get('titlepic')
            article = Article.objects.filter(pk=id).first()
            article.describe = form.cleaned_data.get('describe')
            article.content = form.cleaned_data.get('content')
            article.tags = form.cleaned_data.get('tags')
            # if titlepic:
                # article.titlepic = titlepic
            # 保存数据
            article.save()
            return HttpResponseRedirect(reverse('user:article'))
        else:
            # 验证失败
            article = Article.objects.filter(pk=id).first()
            error = form.errors
            return render(request, 'user/update-article.html', {'article': article, 'error': error})


def args(request, month, day, year):
    """测试"""
    if request.method == 'GET':
        S = '%s年%s月%s日' % (year, month, day)
        return HttpResponse(S)


def logout(request):
    """退出"""
    if request.method == 'GET':
        # 删除session
        request.session.flush()
        return render(request, 'user/login.html')


def price(request):
    """图片上传"""
    if request.method == 'GET':
        return render(request, 'user/price.html')
    if request.method == 'POST':
        # 获取form提交的图片名
        price_name = request.POST.get('price_name')
        # 获取form提交的图片
        price = request.FILES.get('price')
        if not all([price_name, price]):
            msg = '数据不完整'
            return render(request, 'user/price.html', {'msg': msg})
        Prices.objects.create(price_name=price_name,
                              price=price)
        return HttpResponseRedirect(reverse('user:show'))


def show(request):
    if request.method == 'GET':
        id = 3
        pic = Prices.objects.get(pk=id)
        return render(request, 'user/show.html', {'pic': pic})
