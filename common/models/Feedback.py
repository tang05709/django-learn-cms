
from .BaseModel import BaseModel
from django.db import models
from django.urls import reverse

class Feedback(BaseModel):
    STATUS = [
        [0, '正常'],
        [9, '禁用'],
    ]
    title = models.CharField(max_length=255, verbose_name = "标题")
    content = models.TextField(verbose_name = "内容")
    source = models.CharField(max_length=255, null=True, blank=True, verbose_name = "来源")
    ip = models.CharField(max_length=50, null=True, blank=True, verbose_name = "ip")
    status = models.SmallIntegerField(default = 0, choices = STATUS, db_index = True, verbose_name = "状态")

    def get_absolute_url(self):
        return reverse('backend:feedback-index')
    
    # 调用时返回自身的属性，不然都是显示xx object
    def __str__(self):
        return self.title

    class Meta:
        db_table =  'feedback'