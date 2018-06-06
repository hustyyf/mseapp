from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Room,Rent

# Create your views here.
def index(request):
    return HttpResponse("hello,world! You're at publicroom's index.")

def showAll(request):
    data=1
    
    return JsonResponse(data,safe=False)

@require_http_methods(["POST"])
@csrf_exempt
def createNewRent(request):
    
    ap_room=request.POST.get('room')
    ap_applicant=request.POST.get('applicant')
    ap_startTime=request.POST.get('start_time')
    ap_stopTime=request.POST.get('stop_time')
    ap_aimDate=request.POST.get('aim_date')
    ap_phoneNum=request.POST.get('phone_num')
    ap_applyReason=request.POST.get('apply_reason')
    r=Room.objects.get(name=ap_room)
    r.rent_set.create(applicant=ap_applicant,start_time=ap_startTime,stop_time=ap_stopTime,aim_date=ap_aimDate,phone_num=ap_phoneNum,apply_reason=ap_applyReason)
    return HttpResponse(ap_room)