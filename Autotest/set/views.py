from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.
from set.models import Set



#设置管理
def set_manage(request):

    username = request.session.get('user','')
    set_list = Set.objects.all()


    return render(request,'set/set_manage.html',{'user':username,'sets':set_list})

#用户管理
def set_user(request):
    user_list = User.objects.all()
    username  = request.session.get('user','')
    return render(request,'set/set_user.html',{'user':username,'users':user_list})