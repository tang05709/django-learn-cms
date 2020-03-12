
from .BaseModel import BaseModel
from django.db import models
from .Product import Product
from .Attachment import Attachment

class ProductPhoto(BaseModel):
    product = models.ForeignKey(Product, on_delete = models.DO_NOTHING, verbose_name = "产品")
    photo = models.ForeignKey(Attachment, on_delete = models.DO_NOTHING, verbose_name = "图片")

    class Meta:
        db_table =  'product_photo'