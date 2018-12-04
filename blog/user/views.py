from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render


from django.urls import reverse

from user.models import UserName


def register(request):
    """注册"""
    #  请求是get就返回register页面
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        # 1获取参数
        name = request.POST.get('name')
        # 密码加密
        password = request.POST.get('password')
        password = make_password(password)

        # 2校验参数是否完整 （如果有一个值为空, 那就返回False）
        if not all([name, password]):
            msg = '请填写完整的参数'
            return render(request, 'register.html', {'msg': msg})
        # 3判断数据库中是否存在该name用户
        if UserName.objects.filter(username=name).first():
            msg = '该账号已经注册，请登录'
            return render(request, 'login.html', {'msg': msg})
        # 以上验证通过 就创建数据 保存在数据库中
        UserName.objects.create(username=name,
                                password=password)
        return HttpResponseRedirect(reverse('user:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 1. 验证参数是否完整
        if not all(['name', 'password']):
            msg = '信息不完整'
            return render(request, 'login.html', {'msg': msg})
        # 2. 验证name是否被注册
        user = UserName.objects.filter(username=username).first()
        if not user:
            msg = '用户不存在'
            return render(request, 'login.html', {'msg': msg})
        # 3.验证密码是否正确
        if password != user.password:
            msg = '密码不正确'
            return render(request, 'login.html', {'msg': msg})
        # 4.实现登录

        request.session['user_id'] = user.id
        return HttpResponseRedirect(reverse('user:index_back'))


def index_back(request):
    if request.method == 'GET':
        return render(request, 'indexs.html')
