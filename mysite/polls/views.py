from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,JsonResponse
from django.core import serializers

from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:2]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

#get the detail of questions
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

#page for returning the results of questions
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

#page for votes
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def list(request):
    #tomcats=Question.objects.all().values_list('question_text','pub_date')
    data=serializers.serialize("json",Question.objects.all())
    return JsonResponse(data,safe=False)