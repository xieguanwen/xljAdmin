# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from models import SendOrder

class MainDashboard(object):
    widgets = [
        [
            {"type": "html", "title": "welcome", "content": "<h3> Welcome to xiaolajiao admin </h3><p>Join Online qq: <br/>QQ Qun : 279634882</p>"},
        ]
    ]
xadmin.site.register(views.website.IndexView, MainDashboard)

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSetting(object):
    global_search_models = [SendOrder]
    global_models_icon = {SendOrder: 'fa fa-user'}
    menu_style = 'default'#'accordion'
xadmin.site.register(views.CommAdminView, GlobalSetting)

class SendOrderAdmin(object):
    list_display = ("send_id","order_id","send_count","status","send_time")
    list_display_links = ("send_id",)
    list_per_page = 20

    # raw_id_fields = ("order_id",)

    search_fields = ['order_id__order_sn']

    show_detail_fields = ('order_id',)
    list_editable = ('send_count','status')
    save_as = True

    list_filter = ("send_count","send_time")
    reversion_enable = True

xadmin.site.register(SendOrder,SendOrderAdmin)

# class testAdmin(admin.ModelAdmin):
#     list_filter = ("aaa",)

