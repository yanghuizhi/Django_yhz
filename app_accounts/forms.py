# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/26 4:47 下午

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# 继承UserCreationForm，并创建邮件服务
class SignUpForm(UserCreationForm):
    email = forms.CharField(
        max_length=254,
        required=True,
        widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email',
                  'password1', 'password2')