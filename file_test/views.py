from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import time

# Create your views here.
def index(request):

    return HttpResponse('首页')

def reindex(request):
    return redirect('index/')
def page(request):

    return render(request,'file_oi/upload_page.html')

def data(request):

    # 获取上传文件的名
    file = request.FILES.get('file')
    # fi = request.POST.get('file')

    filename = str(int(time.time()))+"."+file.name.split('.').pop()

    # 保存到本地
    f = open('./static/img/'+filename,'wb+')

    # 分段存储文件
    # file.chunks() 代表每一段
    for i in file.chunks():
        f.write(i)
    f.close()

    return HttpResponse('上传文间函数')

# 设置cookie
def set_cookie(request):
    # set_cookie(key,values)
    response = HttpResponse('设置cookie')
    response.set_cookie('key','123456')
    return response
def get_cookie(request):
    ret = request.COOKIES.get('key')
    print(ret)

    return HttpResponse('获得cookie的值{}'.format(ret))

# 设置session
def set_session(request):
    request.session['name'] = 'lk'

    return HttpResponse('设置session成功')

def get_session(request):
    ret = request.session.get('name')
    print(ret)

    return HttpResponse('获取session值：{}'.format(ret))

def spage(request):
    data={}
    data['item1'] = 'lk'
    list1 = ['jiang','xiangyun']
    html = '<h1>天津包子</h1>'
    js = '<script>alert("great")</script>'
    return render(request,'file_oi/tmp.html',{'info':data,'list1':list1,'html':html,'js':js})