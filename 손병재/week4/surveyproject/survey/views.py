from asyncio.windows_events import NULL
from django.shortcuts import render
from .models import Survey, Answer

# Create your views here.

def home(request):
    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]
    return render(request, "survey/home.html", {'survey': survey})

def show_result(request):
    survey_idx_ = request.GET["survey_idx"]
    survey = Survey.objects.filter(survey_idx = survey_idx_)[0]

    answerList = list(Answer.objects.filter(survey_idx = survey_idx_))

    surveyResult = {
        survey.ans1 : 0,
        survey.ans2 : 0,
        survey.ans3 : 0,
        survey.ans4 : 0,
    }

    for answer in answerList:
        surveyResult[answer.ans] += 1

    return render(request, "survey/result.html", {"surveyResult" : surveyResult})

def save_survey(request):
    survey_idx_ = request.POST["survey_idx"]

    dto = Answer(survey_idx=int(survey_idx_), ans = request.POST["ans"] )
    dto.save()

    return render(request, "survey/complete.html", {'survey_idx': survey_idx_})
    

