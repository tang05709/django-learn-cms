from .BaseModel import BaseModel
from django.db import models
from django.urls import reverse
from .Category import Category
from .Attachment import Attachment

class Product(BaseModel):
    STATUS = [
        [0, '正常'],
        [1, '推荐'],
        [2, '置顶'],
        [9, '禁用'],
    ]
    category = models.ForeignKey(Category, on_delete = models.DO_NOTHING, verbose_name = "栏目")
    title = models.CharField(max_length=255, verbose_name = "标题")
    status = models.SmallIntegerField(default = 0, choices = STATUS, db_index = True, verbose_name = "状态")
    price = models.DecimalField(max_digits = 11, decimal_places = 2, default = 0, verbose_name = "价格")
    seo_title = models.CharField(max_length=255, null=True, blank=True, verbose_name = "seo标题")
    seo_keywords = models.CharField(max_length=255, null=True, blank=True, verbose_name = "seo关键字")
    seo_description = models.CharField(max_length=255, null=True, blank=True, verbose_name = "seo描述")
    click = models.IntegerField(default = 0, verbose_name = "点击量")
    sort = models.IntegerField(default = 0, verbose_name = "排序")
    photos = models.ManyToManyField(Attachment, through='ProductPhoto', through_fields=('product', 'photo'), related_name = "photos", blank=True, verbose_name = "画册") #symmetrical = False
    content = models.TextField(null=True, blank=True, verbose_name = "详情")

    def get_absolute_url(self):
        return reverse('backend:product-index')
    
    # 调用时返回自身的属性，不然都是显示xx object
    def __str__(self):
        return self.title

    class Meta:
        db_table =  'product'