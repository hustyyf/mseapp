from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('all/',views.showAll,name='showall'),
    path('creat_new_rent/',views.createNewRent,name='creatRent')
]