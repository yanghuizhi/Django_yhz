"""Django_Learn_YHZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from .settings import MEDIA_ROOT
from app_blog import views as blog_view
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from app_test import views as test_view
from boards import views as boards_views
from django.conf.urls import url, include


urlpatterns = [
    path('admin/', admin.site.urls),



    # 测试学习类
    # path('learn/', test_view.learn_1),
    # path('learn/<offset>/', test_view.learn_3),
    # path('learn4/', test_view.learn_4),
    # path('learn5/', test_view.search_form),
    # path('learn6/', test_view.learn_6),
    # path('learn66/', test_view.login_action),

    # boards 博客系统
    # path('boards/', include('boards.urls', namespace='boards'))
    path('home/', boards_views.BoardListView.as_view(), name='home'),
    re_path(r'boards/(?P<pk>\d+)/', boards_views.TopicListView.as_view(), name='board_topics'),
    re_path(r'boards/(?P<pk>\d+)/new/', boards_views.new_topic, name='new_topic'),
    # 主题回复列表
    re_path(r'boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/', boards_views.PostListView.as_view(), name='topic_posts'),
    re_path(r'boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/', boards_views.reply_topic, name='reply_topic'),
    re_path(r'boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/',
            boards_views.PostUpdateView.as_view(), name='edit_post'),

    # accounts 账户系统 ( +boards )
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(),
         name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'), name='login'),
    # 密码重置内置视图
    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'),
         name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    re_path('reset/<uidb64>/<token>[0-9A-Za-z ]{1,13}-[0-9A-Za-z]{1,20}/', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'),
            name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
    # 密码更改视图
    path('settings/password/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html'),
         name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'),
         name='password_change_done'),
    # 我的账户视
    path('settings/account/',
         accounts_views.UserUpdateView.as_view(), name='my_account'),
]