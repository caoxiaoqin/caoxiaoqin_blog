"""blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import static
from django.contrib import admin
from utils.upload_images import upload_image

from blogs.settings import MEDIA_URL, MEDIA_ROOT
from web import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls', namespace='user')),
    url(r'^web/', include('web.urls', namespace='web')),
    # kindeditor编辑器上传图片地址
    url(r'^util/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    # 直接跳转web/index页面
    url(r'^$', views.index)
]


# 目的是为了告诉Django  在MEDIA_URL路径下 找media文件的静态路径
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
