# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Growing(models.Model):
    growingId = models.AutoField(primary_key=True,verbose_name="成长编号")  # Field name made lowercase.
    user_id = models.IntegerField(verbose_name="用户编号")
    score = models.IntegerField(verbose_name="总分")
    addTime = models.DateTimeField(verbose_name="创建时间")  # Field name made lowercase.
    updateTime = models.DateTimeField(verbose_name="更新时间")  # Field name made lowercase.
    fraction = models.IntegerField(verbose_name="分数")

    class Meta:
        managed = False
        db_table = 'growing'
        verbose_name = _('growing name')
        verbose_name_plural = _('growing name')


    def __unicode__(self):
        return self.score



class GrowingType(models.Model):
    growingTypeId = models.AutoField(primary_key=True,verbose_name="生成编号")  # Field name made lowercase.
    name = models.CharField(max_length=50,verbose_name="成长类型名称")
    description = models.CharField(max_length=255, blank=True, null=True,verbose_name="描述")
    addTime = models.DateTimeField(blank=True, null=True,verbose_name="创建时间")  # Field name made lowercase.
    fraction = models.IntegerField(verbose_name="分数")

    class Meta:
        managed = False
        db_table = 'growing_type'
        verbose_name = _('growing type name')
        verbose_name_plural = _('growing type name')

    def __unicode__(self):
        return unicode(self.name)


class GrowthPoints(models.Model):
    growthPointsId = models.AutoField(primary_key=True,verbose_name="生长分记录编号")  # Field name made lowercase.
    growingTypeId = models.ForeignKey(GrowingType,db_column='growingTypeId',verbose_name="生长类型") #models.IntegerField()  # Field name made lowercase.
    addTime = models.DateTimeField(blank=True, null=True,verbose_name="创建时间")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'growth_points'
        verbose_name = _('growth points name')
        verbose_name_plural = _('growth points name')

    def __unicode__(self):
        return self.growthPointsId

class RankType(models.Model):
    rankTypeId = models.AutoField(primary_key=True,verbose_name="会员等级类型")  # Field name made lowercase.
    name = models.CharField(max_length=50, blank=True, null=True,verbose_name="等级名称")
    description = models.CharField(max_length=255, blank=True, null=True,verbose_name="描述")
    addTime = models.DateTimeField(blank=True, null=True,verbose_name="创建时间")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rank_type'
        verbose_name = _('rank type name')
        verbose_name_plural = _('rank type name')

    def __unicode__(self):
        return unicode(self.name)

class MemberBenefits(models.Model):
    memberBenefitsId = models.AutoField(primary_key=True,verbose_name="会员优惠编号")  # Field name made lowercase.
    rankTypeId = models.ForeignKey(RankType,db_column="rankTypeId",verbose_name="会员等级类型")  # Field name made lowercase.
    name = models.CharField(max_length=100,verbose_name="优惠名")
    description = models.CharField(max_length=255, blank=True, null=True,verbose_name="描述")
    addTime = models.DateTimeField(blank=True, null=True,verbose_name="创建时间")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member_benefits'
        verbose_name = _('member benefits name')
        verbose_name_plural = _('member benefits name')

    def __unicode__(self):
        return unicode(self.name)

class SignRecord(models.Model):
    signRecordId = models.AutoField(primary_key=True,verbose_name="注册记录编号")  # Field name made lowercase.
    user_id = models.IntegerField(verbose_name="用户id")
    ip = models.CharField(max_length=50, blank=True, null=True,verbose_name="IP地址")
    addTime = models.DateTimeField(blank=True, null=True,verbose_name="创建时间")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sign_record'
        verbose_name = _('sign record name')
        verbose_name_plural = _('sign record name')

    def __unicode__(self):
        return self.signRecordId


class VipRank(models.Model):
    vipRankId = models.AutoField(primary_key=True,verbose_name="会员等级编号")  # Field name made lowercase.
    rankTypeId = models.ForeignKey(RankType,db_column="rankTypeId",blank=True, null=True,verbose_name="会员等级类型")  # Field name made lowercase.
    user_id = models.IntegerField(verbose_name="用户id")
    score = models.IntegerField(blank=True, null=True,verbose_name="总分")
    addTime = models.DateTimeField(verbose_name="创建时间")  # Field name made lowercase.
    updateTime = models.DateTimeField(verbose_name="更新时间")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vip_rank'
        verbose_name = _('vip rank name')
        verbose_name_plural = _('vip rank name')


class Welfare(models.Model):
    welfareId = models.AutoField(primary_key=True,verbose_name="福利编号")  # Field name made lowercase.
    name = models.CharField(max_length=100,verbose_name="福利名称")
    description = models.CharField(max_length=255, blank=True, null=True,verbose_name="描述")
    addTime = models.DateTimeField(blank=True, null=True,verbose_name="创建时间")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'welfare'
        verbose_name = _('welfare name')
        verbose_name_plural = _('welfare name')

    def __unicode__(self):
        return unicode(self.name)

class RankWelfare(models.Model):
    rankTypeId = models.ForeignKey(RankType,db_column="rankTypeId",verbose_name="会员等级类型")  # Field name made lowercase.
    welfareId = models.ForeignKey(Welfare,db_column="welfareId",verbose_name="福利编号")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rank_welfare'
        verbose_name = _('rank welfare name')
        verbose_name_plural = _('rank welfare name')