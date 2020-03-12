
from .BaseModel import BaseModel
from django.db import models
from django.urls import reverse

class AdvPosition(BaseModel):
    # 自定义模型管理器
    # advPositiionObj = models.Manager()
    STATUS = [
        [0, '正常'],
        [9, '禁用'],
    ]
    name = models.CharField(max_length=255, verbose_name = '广告位名称')
    status = models.SmallIntegerField(default = 0, choices = STATUS, db_index = True, verbose_name = "状态")

    def get_absolute_url(self):
        return reverse('backend:adv-position-index')
    
    # 调用时返回自身的属性，不然都是显示xx object
    def __str__(self):
        return self.name

    class Meta(BaseModel.Meta):
        db_table =  'adv_position'