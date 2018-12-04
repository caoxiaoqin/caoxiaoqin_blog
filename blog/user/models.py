from django.db import models


class UserName(models.Model):
    """用户模型"""
    username = models.CharField(max_length=10, unique=True, null=False, verbose_name='用户')
    password = models.CharField(max_length=255, unique=True, verbose_name='密码')
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blogs'
