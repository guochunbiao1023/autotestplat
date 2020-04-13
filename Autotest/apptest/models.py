from django.db import models
from product.models import Product
# Create your models here.
class Appcase(models.Model):
    product = models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True)#关联产品Id
    appcasename = models.CharField('用例名称',max_length=200)#测试用例名称
    appresult = models.CharField('测试结果')#测试结果
    apptester = models.CharField('测试负责人',max_length=200)#执行人
    create_time = models.DateTimeField('创建时间',auto_now=True)#创建时间，自动获取当前时间
    class Meta:
        verbose_name = '测试用例'
        verbose_name_plural = 'app测试用例'
    def __str__(self):
        self.appcasename


class Appcasestep(models.Model):
    appcase = models.ForeignKey('appcase.Appcase',on_delete=models.CASCADE) #关联接口ID
    appcasestep = models.CharField('测试步骤',max_length=200)#测试步骤
    apptestobjname = models.