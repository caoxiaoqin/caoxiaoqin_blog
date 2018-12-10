from django.db import models


class UserName(models.Model):
    """用户模型"""
    username = models.CharField(max_length=10, unique=True, null=False, verbose_name='用户')
    password = models.CharField(max_length=255, unique=True, verbose_name='密码')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blogs'


class Article(models.Model):
    """文章"""
    title = models.CharField(max_length=100, unique=True, null=False, verbose_name='文章标题')
    describe = models.CharField(max_length=255, unique=True, verbose_name='文章描述', null=False)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField(verbose_name='文章内容')
    keywords = models.CharField(max_length=100, null=False)
    tags = models.CharField(max_length=20, null=False)
    art_user = models.ForeignKey(UserName, verbose_name='用户与文章的一对多关系')

    class Meta:
        db_table = 'article'


class Prices(models.Model):
    price_name = models.CharField(null=False, max_length=100, verbose_name='图片名称')
    price = models.ImageField(null=False, upload_to='price')

    class Meta:
        db_table = 'prices'
