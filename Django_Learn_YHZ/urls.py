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
from app_boards import views as boards_view
from app_accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from app_test import views as test_view
# app_name='Django_Learn_YHZ.urls'

urlpatterns = [
    path('learn/',test_view.learn_1),
    path('learn/<offset>/',test_view.learn_3),
    path('learn4/',test_view.learn_4),
    path('learn5/',test_view.search_form),
    path('learn6/',test_view.learn_6),
    path('learn66/',test_view.login_action),


    path('admin/', admin.site.urls),
    path('blog/', blog_view.index),
    path('posts/<pk>/', blog_view.detail, name='detail'),

    # app_boards 博客系统
    path('home/', boards_view.BoardListView.as_view(), name='home'),
    # path('boards/<int:pk>/', boards_view.board_topics, name='board_topics'),
    path('boards/<pk>/new/', boards_view.new_topic, name='new_topic'),
    path('boards/<pk>/', boards_view.TopicListView.as_view (),
         name='board_topics'),
    # 片段
    path('boards/(<pk>/topics/<topic_pk>/',
         boards_view.PostListView.as_view(), name='topic_posts'),

    # app_accounts 拆分上述博客系统的账户系统
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(),
         name='logout'),
    path('login/', auth_views.LoginView.as_view(
        template_name='app_accounts/login.html'), name='login'),

    path('reset/', auth_views.PasswordResetView.as_view(
        template_name='app_accounts/password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'),
        name='password_reset'),
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='app_accounts/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>[0-9A-Za-z ]{1,13}-[0-9A-Za-z]{1,20}/', auth_views.PasswordResetConfirmView.as_view(
        template_name='app_accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'app_accounts/password_reset_complete.html'),
        name = 'password_reset_complete'),
    # 修改密码
    path('settings/password/', auth_views.PasswordChangeView.as_view(
        template_name='app_accounts/password_change.html'),
        name='password_change'),
    path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='app_accounts/password_change_done.html'),
        name='password_change_done'),

    # 主题回复
    path('boards/<pk>/topics/<topic_pk>/', boards_view.topic_posts, name='topic_posts'),
    path('boards/<pk>/topics/<topic_pk>/reply/', boards_view.reply_topic, name='reply_topic'),
    path('boards/<pk>/topics/<topic_pk>/posts/<post_pk>/edit/', boards_view.PostUpdateView.as_view(), name='edit_post'),

    # 我的账户视图
    path('settings/account/',
         accounts_views.UserUpdateView .as_view(), name='my_account'),
]

# 路由规则学习
# path('article-(\d+)-(\d+).html',views.article),
# path('article-(?P<article_type_id>\d+)-(?P<category_id>\d+).html',views.article, name='article'),