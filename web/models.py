from django.db import models
from rbac.models import UserInfo as RbacUserInfo


# Create your models here.
class CollageInfo(models.Model):
    collage = models.CharField(verbose_name="学院", max_length=32)

    def __str__(self):
        return self.collage


class UserInfo(RbacUserInfo):
    username = models.CharField(verbose_name="姓名", max_length=16)
    collage = models.ForeignKey(verbose_name="学院", to="CollageInfo", to_field="id", on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Task(models.Model):
    Tid = models.CharField(verbose_name="项目编号", max_length=64)
    title = models.CharField(verbose_name="项目名称", max_length=32)
    collage = models.ForeignKey(verbose_name="学院", to="CollageInfo", to_field="id", on_delete=models.CASCADE)
    owner = models.CharField(verbose_name="负责人", max_length=32)
    file = models.FileField(verbose_name="相关文件", max_length=128, upload_to='File/')


class TaskRecord(models.Model):
    task = models.ForeignKey(verbose_name="所跟进项目", to='Task', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='跟进日期', auto_now_add=True)
    note = models.TextField(verbose_name="跟进内容")
