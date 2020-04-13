from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from app.models import Apitest,ApiStep,Apis
from django.contrib.auth import authenticate,login
# Create your views here.
def login(request):
    return render(request,'login.html')
def login_action(request):
    if request.POST:
        username = password = ''
        print('------------------------1')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user']  = username
            print('------------------------')
            respone = HttpResponseRedirect('/home/')
            return respone
        else:
            return render(request,'login.html',{'error':'username or password error'})

    # else:
    #      context = {}
    #      return  render(request,'login.html',context)
    return render(request,'login.html')


def home(request):
    return render(request,'home.html')
def logout(resquest):
    auth.logout(resquest)
    return render(resquest,'login.html')

#接口管理
@login_required
def apiTest_manage(request):
    username = request.session.get('user', '')  # 读取浏览器的Session
    apiTest_list = Apitest.objects.all()#读取所有流程接口数据


    return render(request,'app/apitest_manage.html',{'user':username,'apiTests':apiTest_list})#定义流程接口数据的变量并返回到前端

#接口步骤管理
@login_required
def apiStep_manage(request):
    username = request.session.get('user', '')  # 读取浏览器的Session
    apiStep_list = ApiStep.objects.all()

    return render(request, 'app/apistep_manage.html', {'user': username, 'apiSteps': apiStep_list})

#单一接口管理
@login_required
def apis_manage(request):
    print('---------------------------')
    username = request.session.get('user','')
    print(username)
    apis_list = Apis.objects.all()
    return render(request,"app/apis_manage.html",{'user':username,'apiss':apis_list})