from django.db import models
from product.models import Product
# Create your models here.
#流程接口管理功能后台开发
class Apitest(models.Model):
    #关联产品id，其中product是应用名，Product是product应用的表明
    product = models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)
    apiTestName = models.CharField('流程接口名称', max_length=64)  # 流程接口测试场景
    apiTestdesc = models.CharField('描述', max_length=200)  # 流程接口描述
    apiTester = models.CharField('测试负责人', max_length=200)  # 执行人
    apiTestResult = models.BooleanField('测试结果') #流程接口测试结果
    createTime = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    class meta:
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程接口场景'

    def __str__(self):
        return self.apiTestName

class ApiStep(models.Model):

    apiTest = models.ForeignKey(Apitest,on_delete=models.CASCADE,null=True) #关联接口ID
    apiStep = models.CharField('测试步骤', max_length=100, null=True)  # 测试步骤
    apiName = models.CharField('接口名称',max_length=100)#接口标题
    apiUrl = models.CharField('url地址',max_length=200)#地址
    apiParamValue = models.CharField('请求参数和值',max_length=800)#参数和值
    REQUEST_METHOD = (('get','get'),('post','post'),('put','put'),('delete','delete'),('patch','patch'))
    apiMethod = models.CharField(verbose_name='请求方法',choices=REQUEST_METHOD,default='get',max_length=200,null=True)#请求方法
    apiResult = models.CharField('预测结果',max_length=200)#预期结果
    apiRespose = models.CharField('响应数据',max_length=5000,null=200)#响应数据
    apiStatus = models.BooleanField('是否通过')#测试结果
    createTime = models.DateTimeField('创建时间', auto_now=True)  # 创建时间，自动获取当前时间

    def _str__(self):
        return self.apiName

#单一接口管理功能后台开发
class Apis(models.Model):
    product = models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)#关联产品id
    apiname = models.CharField('接口名称',max_length=100)#接口标题
    apiurl = models.CharField('url地址',max_length=200)#地址
    apiparamvalue = models.CharField('请求参数',max_length=800)#请求参数和值
    REQUEST_MEHOD = (('0','get'),('1','post'),('2','put'),('3','delete'),('4','patch'))
    apimethod = models.CharField(verbose_name='请求方法',choices=REQUEST_MEHOD,default=0,max_length=200)#请求方法
    apiresult = models.CharField('预期结果',max_length=200)#预期结果
    apistatus = models.BooleanField('是否通过')#测试结果
    create_time = models.DateTimeField('创建时间',auto_now=True)#创建时间，自动获取当前时间

    class Meta:
        verbose_name = '单一场景接口'
        verbose_name_plural = '单一接口场景'
    def __str__(self):
        return self.apiname










