from django.db import models
from django.utils import timezone
from pilkit.processors import ResizeToFill
from django.core.validators import MinValueValidator

from common.core.models import DbAuditModel, upload_directory_path, AutoCleanFileMixin
from common.fields.image import ProcessedImageField
from system.models import UserInfo


class Part(models.Model):
    part_number = models.CharField('零件号', max_length=50, unique=True)
    name = models.CharField('品名', max_length=100)
    unit = models.CharField('单位', max_length=20)
    drawing_number = models.CharField('图号', max_length=50)
    spec1 = models.CharField('规格1', max_length=50, blank=True)
    spec2 = models.CharField('规格2', max_length=50, blank=True)
    spec3 = models.CharField('规格3', max_length=50, blank=True)
    spec4 = models.CharField('规格4', max_length=50, blank=True)
    spec5 = models.CharField('规格5', max_length=50, blank=True)
    spec6 = models.CharField('规格6', max_length=50, blank=True)
    spec7 = models.CharField('规格7', max_length=50, blank=True)
    spec8 = models.CharField('规格8', max_length=50, blank=True)
    spec9 = models.CharField('规格9', max_length=50, blank=True)
    price = models.DecimalField('价格', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = '零件主文件'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"