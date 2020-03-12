
from .BaseModel import BaseModel
from django.db import models

class Attachment(BaseModel):
    STATUS = [
        [0, '正常'],
        [9, '禁用'],
    ]
    original_name = models.CharField(max_length=255, verbose_name = "原始名称")
    name = models.CharField(max_length=255, verbose_name = "新名称")
    url = models.CharField(max_length=255, verbose_name = "图片存放地址")
    status = models.SmallIntegerField(choices = STATUS, db_index = True, verbose_name = "状态")

    def __str__(self):
        return self.url

    class Meta:
        db_table =  'attachment'
