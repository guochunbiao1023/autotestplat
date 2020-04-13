from django.contrib import admin

# Register your models here.
from bug.models import Bug
class BugAdmin(admin.ModelAdmin):
    list_display = ['bugname','bugdetail','bugstatus','buglevel','bugcreater','bugssign','create_time','id']



admin.site.register(Bug)#把bug管理模块注册到Django admin后台并能显示
