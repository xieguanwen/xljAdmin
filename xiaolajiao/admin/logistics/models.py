# -*- coding: utf-8 -*-
from django.db import models
from order.models import OrderInfo

class SendOrder(models.Model):
    send_id = models.AutoField(verbose_name=u"发送编号",primary_key=True)
    order_id = models.ForeignKey(OrderInfo,db_column='order_id',verbose_name=u"订单id")
    send_time = models.DateField(verbose_name=u"发送时间",blank=True)
    send_count = models.SmallIntegerField(verbose_name=u"发送次数")
    send_update_time = models.DateField(verbose_name=u"发送更新时间",blank=True)
    status = models.SmallIntegerField(default=0,verbose_name=u"状态")

    def __unicode__(self):
        return self.send_id

    class Meta:
        db_table = 'shouji_send_order'
        verbose_name=u"发送订单记录"