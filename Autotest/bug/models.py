from django.db import models
from product.models import Product
# Create your models here.

class Bug(models.Model):
    product = models.ForeignKey('product.Product',on_delete=models.CASCADE,null=True) #关联产品ID
    bugname = models.CharField('bug名称',max_length=64) #bug名称
    bugdetail = models.CharField('详情',max_length=200) #详情
    BUG_DETAIL = (('激活','激活'),('已解决','已解决'),('已关闭','已关闭'))
    bugstatus = models.CharField(verbose_name='解决状态',choices=BUG_DETAIL,default='激活',max_length=200,null=True)#解决状态
    BUG_LEVEL = (('1','1'),('2','2'),('3','3'))
    buglevel = models.CharField(verbose_name='严重程度',choices=BUG_LEVEL,max_length=200,null=True)#严重程度
    bugCreater = models.CharField('创建',max_length=200)#创建人
    bugassign = models.CharField('分配给',max_length=200)#分配给
    create_time = models.DateTimeField('创建时间',auto_now=True)#创建时间
    class Meta:
        verbose_name = 'bug管理'
        verbose_name_plural = 'bug管理'
    def __str__(self):
        return  self.bugname




