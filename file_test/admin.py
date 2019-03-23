from django.contrib import admin
from .models import HeroInfo,BookInfo
# Register your models here.

@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    # 每页显示数据条数
    list_per_page = 5
    # 显示字段
    # btitle
    # bdate
    # bread
    # bcomment
    # is_delete
    list_display = ['btitle','bdate','bread','bcomment','is_delete']


@admin.register(HeroInfo)
class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 5
    # hname
    # hsex
    # hbook
    # is_delete
    list_display = ["hname","hsex","hbook","is_delete"]