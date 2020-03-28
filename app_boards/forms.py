# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2020/3/26 4:47 下午

from django import forms
from .models import Topic
from .models import Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
        attrs={'rows': 5, 'placeholder': 'What is on your mind?'}),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']

# 给回帖创建一个新的表单
class PostForm(forms.ModelForm):
    pass

    class Meta:
        model = Post
        fields = ['message', ]