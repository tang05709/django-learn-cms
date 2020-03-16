
from .BaseModel import BaseModel
from django.db import models
from django.urls import reverse

class Category(BaseModel):
    STATUS = [
        [0, '正常'],
        [9, '禁用'],
    ]
    MODULE = [
        ['posts', '单页面'],
        ['article', '文章'],
        ['product', '产品'],
    ]
    name = models.CharField(max_length=255, verbose_name = "栏目名称")
    module = models.CharField(max_length=255, choices = MODULE, verbose_name = "栏目类型")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete = models.SET_NULL, related_name='children', verbose_name = "父级")
    seo_title = models.CharField(max_length=255, null=True, blank=True, verbose_name = "seo标题")
    seo_keywords = models.CharField(max_length=255, null=True, blank=True, verbose_name = "seo关键字")
    seo_description = models.CharField(max_length=255, null=True, blank=True, verbose_name = "seo描述")
    sort = models.IntegerField(default = 0, verbose_name = "排序")
    status = models.SmallIntegerField(default = 0, choices = STATUS, db_index = True, verbose_name = "状态")
    content = models.TextField(null=True, blank=True, verbose_name = "详情")

    def get_absolute_url(self):
        return reverse('backend:category-index')
    
    # 调用时返回自身的属性，不然都是显示xx object
    def __str__(self):
        return self.name

    class Meta:
        db_table =  'category'