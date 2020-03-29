import datetime

from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect


# Create your views here.

def learn_1(request):
    """
    静态 URL 学习
    :param request: 必须作为第一个参数传给视图，约定俗成的对象
    :return: HttpResponse实例
    """
    return HttpResponse("hello world")


def learn_2(request):
    now = datetime.datetime.now()
    html = f"It is now {now}"
    return HttpResponse(html)


def learn_3(request, offset):
    """
    动态 URL 学习
    :param request:
    :param offset:  动态URL配置
    :return:
    """
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dnt = datetime.datetime.now()
    dnts= dnt + datetime.timedelta(hours=offset)
    html = f"<h2>原始时间为 {dnt}, \n " \
           f"<h2>你输入了 {offset} 这个参数, \n" \
           f"<h2>时间将会变成 {dnts}."
    return HttpResponse(html)

from django.template.loader import get_template
def learn_4(request):
    """
    模版使用学习,加载模板、填充上下文
    """
    now = datetime.datetime.now()
    # 替换硬编码的模板路径, 了解 Django 加载 及在浏览器中渲染模板的过程。
    # t = get_template('app_test/learn_4.html')
    # html = t.render({'current_date': now})
    # return HttpResponse(html)
    # 有一种更为简单的方式,而不自己动手加载模板、创建 Context 和 HttpResponse 对象
    # render(请求对象, 模板名称, opt)
    # opt：可选字段，用于创建传给模板的上下文，默认空，若不指定参数，render() 使用一个空字典。
    return render(request, 'app_test/learn_4.html', {'current_date': now})


def search_form(request):
    # 表单处理学习
    return render(request, 'app_test/search_form.html')

from .models import Book
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render(request, 'app_test/search_results.html',
                          {'books': books, 'query': q})
            return render(request, 'app_test/search_form.html',
                          {'error': error})


def learn_6(request):
    return render(request,'app_test/login.html')

from django.contrib import auth
from django.contrib.auth.decorators import login_required
# @login_required
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将 session 信息记录到浏览器
            response = HttpResponseRedirect('/login_action/')
            return response
        else:
            return render(request, 'app_test/login2.html',
                      {'error': 'username or passworderror!'})
