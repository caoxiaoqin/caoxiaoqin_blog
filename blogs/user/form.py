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


class AddArticle(forms.Form):
    title = forms.CharField(max_length=100,  required=True,
                            error_messages={
                                'required': '标题必填',

                                'max_length': '最大字段长度不超过100个字符'
                            })
    content = forms.CharField(min_length=5, required=True,
                              error_messages={
                                'required': '标题必填',
                                'min_length': '最小字段不小于5个字符',
                            })
    describe = forms.CharField(max_length=255, required=True,
                               error_messages={
                                'required': '描述必填',
                                'max_length': '最大字段长度不超过255个字符'
                            })
    keywords = forms.CharField(max_length=100,
                               error_messages={

                                'max_length': '最大字段长度不超过100个字符'
                           })
    tags = forms.CharField(max_length=20,
                           error_messages={

                                'max_length': '最大字段长度不超20个字符'
                            })


class UpdateArticle(forms.Form):
    title = forms.CharField(max_length=100,  required=True,
                            error_messages={
                                'required': '标题必填',
                                'max_length': '最大字段长度不超过100个字符'
                            })
    content = forms.CharField(required=True,
                              error_messages={
                                'required': '标题必填',
                            })
    describe = forms.CharField(max_length=255, min_length=5, required=True,
                               error_messages={
                                'required': '描述必填',
                                'min_length': '最小字段不小于5个字符',
                                'max_length': '最大字段长度不超过255个字符'
                            })
    tags = forms.CharField(max_length=20,
                           error_messages={
                                'max_length': '最大字段长度不超过255个字符'
                            })

    keywords = forms.CharField(max_length=100,
                               error_messages={
                                    'max_length': '最大字段长度不超过255个字符'
                                })