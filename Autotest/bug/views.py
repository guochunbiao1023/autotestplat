from django.shortcuts import render
from bug.models import Bug
#bug管理
def bug_manage(request):
    username = request.session.get('user','')
    bug_list = Bug.objects.all()
    return render(request,'bug/bug_manage.html',{'user':username,'bugs':bug_list})

# Create your views here.
