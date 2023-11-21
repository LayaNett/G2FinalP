from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Character, Question, Answer

def index(request):
    character_list = Character.objects.order_by("id")[:5]
    context = {"character_list": character_list}
    return render(request, "polls/index.html", context)

def detail(request, character_id):
    try:
        character = Character.objects.get(pk=character_id)
    except Character.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"character": character})

def results(request, charName):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % charName)

def vote(request, charName):
    return HttpResponse("You're voting on question %s." % charName)

def survey(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/survey.html", {"question": question})