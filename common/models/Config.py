from .BaseModel import BaseModel
from django.db import models
from django.urls import reverse

class Config(BaseModel):
    ckey = models.CharField(max_length=255, db_index = True, verbose_name = "配置名称", help_text = "必须是英文")
    cvalue = models.CharField(max_length=255, verbose_name = "配置值")

    def get_absolute_url(self):
        return reverse('backend:config-index')

    # 调用时返回自身的属性，不然都是显示xx object
    def __str__(self):
        return self.ckey

    class Meta:
        db_table =  'config'