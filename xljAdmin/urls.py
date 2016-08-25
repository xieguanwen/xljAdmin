from django.conf.urls import patterns, include, url
from xiaolajiao.direction import urls as directionUrls
import xadmin

urlpatterns = patterns('',
    url(r'^', include(xadmin.site.urls)),
    url(r'^direction/', include(directionUrls)),
)

