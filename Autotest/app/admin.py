from django.contrib import admin

# Register your models here.
from app.models import Apitest,ApiStep,Apis

#Register your model here

class ApiStepAdmin(admin.TabularInline):
    list_display = [
        'apiName',
        'apiUrl',
        'apiParamValue',
        'apiMethod',
        'apiResult',
        'apiStatus',
        'createTime',
        'id',
        'apiTest',
    ]
    model =  ApiStep
    extra = 1


class ApitestAdmin(admin.ModelAdmin):
    list_display = [
        'apiTestName',
        'apiTester',
        'apiTestResult',
        'createTime',
        'id',
    ]
    inlines = [ApiStepAdmin]
admin.site.register(Apitest,ApitestAdmin)

class ApiAdmin(admin.TabularInline):
    list_display = ['apiname','apiurl','apiparavalue','apimethod','apiresult','apistatus','create_time','id','product']

admin.site.register(Apis)