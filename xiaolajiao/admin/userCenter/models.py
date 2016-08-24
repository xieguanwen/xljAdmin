# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Growing(models.Model):
    growingId = models.AutoField(primary_key=True,verbose_name="成长编号")  # Field name made lowercase.
    user_id = models.IntegerField(verbose_name="用户编号")
    score = models.IntegerField(verbose_name="总分")
    addTime = models.DateTimeField(verbose_name="添加时间")  # Field name made lowercase.
    updateTime = models.DateTimeField(verbose_name="更新时间")  # Field name made lowercase.
    fraction = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'growing'


    def __unicode__(self):
        return self.growingId


class GrowingType(models.Model):
    growingTypeId = models.AutoField(primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True, null=True)
    addTime = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.
    fraction = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'growing_type'
        verbose_name = _('growing type name')
        verbose_name_plural = _('growing type name')

    def __unicode__(self):
        return unicode(self.name)


class GrowthPoints(models.Model):
    growthPointsId = models.AutoField(primary_key=True)  # Field name made lowercase.
    growingTypeId = models.ForeignKey(GrowingType,db_column='growingTypeId',verbose_name=u"") #models.IntegerField()  # Field name made lowercase.
    addTime = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'growth_points'

class MemberBenefits(models.Model):
    memberBenefitsId = models.AutoField(primary_key=True)  # Field name made lowercase.
    rankTypeId = models.IntegerField()  # Field name made lowercase.
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    addTime = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member_benefits'


class RankType(models.Model):
    rankTypeId = models.AutoField(primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    addTime = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rank_type'


class RankWelfare(models.Model):
    rankTypeId = models.IntegerField()  # Field name made lowercase.
    welfareId = models.IntegerField()  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rank_welfare'


class SignRecord(models.Model):
    signRecordId = models.AutoField(primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField()
    ip = models.CharField(max_length=50, blank=True, null=True)
    addTime = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sign_record'


class VipRank(models.Model):
    vipRankId = models.AutoField(primary_key=True)  # Field name made lowercase.
    rankTypeId = models.IntegerField(blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField()
    score = models.IntegerField(blank=True, null=True)
    addTime = models.DateTimeField()  # Field name made lowercase.
    updateTime = models.DateTimeField()  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vip_rank'


class Welfare(models.Model):
    welfareId = models.AutoField(primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    addTime = models.DateTimeField(blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'welfare'