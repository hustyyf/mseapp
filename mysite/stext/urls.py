from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='stext_index'),
    path('return/',views.giving),
]