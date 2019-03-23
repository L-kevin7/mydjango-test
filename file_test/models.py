from django.db import models

# Create your models here.
class mide(models.Manager):
    pass
# 图书信息
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20,verbose_name='名称')
    bdate = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0,verbose_name="阅读量")
    bcomment = models.IntegerField(default=0,verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta():
        db_table = 'books' #数据库中显示的表名称
        verbose_name = '图书'# admin 中显示的名称django_admin_log
        verbose_name_plural = verbose_name #显示的复数形式

    def __str__(self):
        #定义每个数据对象的显示信息
        return self.btitle


# 英雄信息
class HeroInfo(models.Model):

    SEX = ((0,'woman'),(1,'man'))

    hname = models.CharField(max_length=20,verbose_name='英雄名')
    hsex = models.SmallIntegerField(choices=SEX,default=0,verbose_name='性别')
    hcontent = models.CharField(max_length=100,null=True,verbose_name='绝招')

    hbook = models.ForeignKey(to=BookInfo,on_delete=models.CASCADE,verbose_name='关联图书')
    is_delete= models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta():
        db_table = 'hero'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):

        return self.hname
