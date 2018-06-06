from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core import serializers

def index(request):
    template = loader.get_template('stext/index.html')
    context={
        
    }
    return HttpResponse(template.render(context,request))

def giving(request):
    st_status=request.POST.getlist('status')
    return HttpResponse(st_status)