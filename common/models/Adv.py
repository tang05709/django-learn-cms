
from .BaseModel import BaseModel
from django.db import models
from django.urls import reverse
from .AdvPosition import AdvPosition
from .Attachment import Attachment

class Adv(BaseModel):
    STATUS = [
        [0, '正常'],
        [9, '禁用'],
    ]
    adv_position = models.ForeignKey(AdvPosition, on_delete = models.DO_NOTHING, verbose_name = "广告位")
    name = models.CharField(max_length=255, verbose_name = "广告名称")
    url = models.CharField(max_length=255, verbose_name = "广告连接")
    image = models.OneToOneField(Attachment, on_delete = models.DO_NOTHING, null=True, blank=True, verbose_name = "图片")
    status = models.SmallIntegerField(default = 0, choices = STATUS, db_index = True, verbose_name = "状态")
    sort = models.IntegerField(default = 0, verbose_name = "排序")
    describe = models.CharField(max_length=255, null=True, blank=True, verbose_name = "广告描述")

    def get_absolute_url(self):
        return reverse('backend:adv-index')

    # 调用时返回自身的属性，不然都是显示xx object
    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table =  'adv'
