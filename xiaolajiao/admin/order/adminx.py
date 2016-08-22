# -*- coding: utf-8 -*-
import xadmin
from django.contrib import admin
from xadmin import views
from models import OrderInfo

class OrderInfoAdmin(object):
    list_display = ('order_id','order_sn','pay_status','add_time')
    list_display_links = ('order_sn',)

    list_search = ('order_sn')
    relfield_style = 'fk-ajax'

xadmin.site.register(OrderInfo,OrderInfoAdmin);
