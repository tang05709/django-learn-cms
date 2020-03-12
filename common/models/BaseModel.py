from django.db import models
from django.utils import timezone
from django.conf import settings

class BaseModel(models.Model):
    #table_prefix = settings.TABLE_PREFIX
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "添加时间")
    updated_at = models.DateTimeField(auto_now = True, verbose_name = "修改时间")

    class Meta:
        abstract = True