import xadmin
from xiaolajiao.admin.userCenter.models import *

# class GrowingAdmin(object):
#     list_display = ('growingId','user_id','score','fraction')
#     list_display_links = ('growingId',)
#
#     # list_search = ('')
#
# xadmin.site.register(Growing,GrowingAdmin)

class GrowingTypeAdmin(object):
    list_display = ('growingTypeId','name')
    list_display_links = ('name',)

    # list_search = ('')

xadmin.site.register(GrowingType,GrowingTypeAdmin)
#
# class GrowthPointsAdmin(object):
#     list_display = ('growthPointsId','growingTypeId')
#     list_display_links = ('growthPointsId',)
#
#     # list_search = ('')
#
# xadmin.site.register(GrowthPoints,GrowthPointsAdmin)
#
# class MemberBenefitsAdmin(object):
#     list_display = ('memberBenefitsId','rankTypeId','name')
#     list_display_links = ('memberBenefitsId',)
#
#     # list_search = ('')
#
# xadmin.site.register(MemberBenefits,MemberBenefitsAdmin)
#
# class RankTypeAdmin(object):
#     list_display = ('rankTypeId','name','description')
#     list_display_links = ('rankTypeId',)
#
#     # list_search = ('')
#
# xadmin.site.register(RankType,RankTypeAdmin)
#
# class RankWelfareAdmin(object):
#     list_display = ('rankTypeId','welfareId')
#     list_display_links = ('rankTypeId',)
#
#     # list_search = ('')
#
# xadmin.site.register(RankWelfare,RankWelfareAdmin)
#
# class SignRecordAdmin(object):
#     list_display = ('signRecordId','user_id','ip')
#     list_display_links = ('signRecordId',)
#
#     # list_search = ('')
#
# xadmin.site.register(SignRecord,SignRecordAdmin)
#
# class VipRankAdmin(object):
#     list_display = ('vipRankId','rankTypeId','user_id')
#     list_display_links = ('vipRankId',)
#
#     # list_search = ('')
#
# xadmin.site.register(VipRank,VipRankAdmin)
#
# class WelfareAdmin(object):
#     list_display = ('welfareId','name')
#     list_display_links = ('welfareId',)
#
#     # list_search = ('')
#
# xadmin.site.register(Welfare,WelfareAdmin)