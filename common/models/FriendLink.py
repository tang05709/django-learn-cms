
from .BaseModel import BaseModel
from django.db import models
from django.urls import reverse
from .Attachment import Attachment

class FriendLink(BaseModel):
    STATUS = [
        [0, '正常'],
        [9, '禁用'],
    ]
    name = models.CharField(max_length=255, verbose_name = "名称")
    logo = models.OneToOneField(Attachment, null=True, blank=True, on_delete = models.DO_NOTHING, verbose_name = "Logo")
    url = models.URLField(max_length=255, verbose_name = "Url", help_text = "格式： https://www.example.com")
    sort = models.IntegerField(default = 0, verbose_name = "排序")
    status = models.SmallIntegerField(default = 0, choices = STATUS, db_index = True, verbose_name = "状态")

    def get_absolute_url(self):
        return reverse('backend:friend-link-index')

    # 调用时返回自身的属性，不然都是显示xx object
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'friend_link'