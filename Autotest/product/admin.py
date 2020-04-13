from django.contrib import admin

from app.models import Apis
from product.models import Product
# Register your models here.
#根据数据库设计生成Django admin后台功能
class ProductAdmin(admin.ModelAdmin):
    list_display = ['productName','productdesc','producter','createTime','id']

    admin.site.register(Product) #把餐品模块注册到django admin并能显示


#加入产品管理字段
class Apisadmin(admin.TabularInline):
    list_display = ['apiname','apiurl','apiparavalue','apimethod','apiresult','apistatus','create_time','id','product']
    model = Apis
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname','productdesc','create_time','id']
    inlines = [Apisadmin]


