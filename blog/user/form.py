# encoding: utf-8
"""
@author: 曹晓芹

"""
from django import forms


class UserNameLogin(forms.Form):
    username = forms.CharField(max_length=12, min_length=2, required=True,
                               error_messages={
                                   'required': '必填',
                                   'max_length': '最大字段长度不超过12个字符',
                                   'min_length': '最小字段不小于2个字符',
                               })
    password = forms.CharField(max_length=12, min_length=2, required=True,
                               error_messages={
                                   'required': '必填',
                                   'max_length': '最大字段长度不超过12个字符',
                                   'min_length': '最小字段不小于2个字符',
                               })