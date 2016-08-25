import views
from django.conf.urls import url

urlpatterns = [
    url('^[/]$',views.index,name="index"),
    url('^index[/]$',views.index,name="index"),
]