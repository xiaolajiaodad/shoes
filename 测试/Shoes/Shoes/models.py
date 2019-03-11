from django.db import models

# Create your models here.
class User(models.Model):
    phone = models.CharField(max_length=11)
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='姓名'
        verbose_name_plural=verbose_name
class Shoes(models.Model):
    size = models.IntegerField()
    color  = models.CharField(max_length=10)
    user = models.ForeignKey(User)
    class Meta:
        verbose_name='鞋子'
        verbose_name_plural=verbose_name


