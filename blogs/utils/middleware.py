# encoding: utf-8
"""
@author: 曹晓芹

"""
import logging
import time

from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from user.models import UserName


class LoginStatusMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """请求"""
        # request.path 获取请求路由
        # 登录和注册是不需要登录验证
        if request.path in ['/user/login/', '/user/register/', '/web/index/',
                            '/web/share/', '/web/list/', 'web/about/', '/web/gbook/',
                            '/web/info/', '/user/price/', '/user/show/']:
            return None
        user_id = request.session.get('user_id')
        # 登录成功
        if user_id:
            # 通过user_id获取用户对象
            user = UserName.objects.filter(pk=user_id).first()
            if user:
                # 给request.user赋值
                request.user = user
                # 如果有用户 那么他就可以访问所有的页面
                return None
            else:
                return HttpResponseRedirect('/user/login/')
        # # 获取请求路由
        # path = request.path
        # # 设置不需要登录验证的url
        # not_need_path = ['/user/login/', '/user/register/']
        # for not_path in not_need_path:
        #     if re.match(not_path, path):
        #         return None
        # 没有登录 就不能访问
        return HttpResponseRedirect('/user/login/')

    # def process_response(self, request, response):
    #     """响应"""
    #     return None


# 获取logging
log = logging.getLogger(__name__)


class LogMiddleware(MiddlewareMixin):
    """log的中间件"""
    def process_request(self, request):
        # 绑定在request上的一个属性 表示访问的时间
        request.init_time = time.time()

    def process_response(self, request, response):
        # 获取url的耗时时间
        count_time = time.time() - request.init_time
        # 响应状态码
        code = response.status_code
        # 请求地址
        path = request.path
        # 请求方式
        method = request.method
        # 响应内容
        try:
            content = response.content
        except:
            content = ''
        # 写入日志中的格式
        log_str = '%s %s %s %s %s ' % (path, method,
                                       code, count_time, content)
        # 交给logger处理的日志
        log.info(log_str)
        # 必须返回response
        return response