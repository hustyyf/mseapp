from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('sender/',views.sender,name='fasongzhe'),
    path('accepter/<int:jieshouzhe_id>detail/',views.jname,name='jname'),
    path('<int:fasongzhe_id>/',views.fasongjieshou,name='fasongjieshou'),
    path('form/',views.post,name='form'),

]
