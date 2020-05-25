from django.conf.urls import url
from .views import *

urlpatterns=[
url(r'^$',home,name='home'),
# url(r'^$',home,name='home'),
url(r'^Agra$',Agra_d,name='Agra'),
url(r'^Aligarh$',Aligarh_d,name='Aligarh'),
url(r'^Kasganj$',Kasganj_d,name='Kasganj'),
url(r'^Kannauj$',Kannauj_d,name='Kannauj'),
url(r'^Farrukhabad$',Farrukhabad_d,name='Farrukhabad'),
url(r'^Auraiya$',Auraiya_d,name='Auraiya'),
url(r'^Mathura$',Mathura_d,name='Mathura'),
url(r'^Hathras$',Hathras_d,name='Hathras'),
url(r'^Etawah$',Etawah_d,name='Etawah'),
url(r'^Firozabad$',Firozabad_d,name='Firozabad'),
url(r'^Mainpuri$',Mainpuri_d,name='Mainpuri'),
url(r'^Etah$',Etawah_d,name='Etah'),
url(r'^edit_Aligarh/(?P<pk>\d+)$',edit_Aligarh,name='edit_Aligarh'),

]
