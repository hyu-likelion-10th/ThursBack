from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from work1.models import Survey, Answer


def home(request):

    survey = Survey.objects.filter(status='y').order_by('-survey_idx')[0]

    return render(request, "survey/list.html", {'survey': survey})


@csrf_protect
def save_survey(request):
   
    survey_idx = request.POST["survey_idx"]
  
    dto = Answer(survey_idx=int(request.POST["survey_idx"]), ans=request.POST["num"])
    
    dto.save()
    return render(request, "survey/success.html")


@csrf_protect
def show_result(request, survey_idx):
    survey = Survey.objects.filter(survey_idx=survey_idx)[0]
    result = {
        survey.ans1:0,
        survey.ans2:0,
        survey.ans3:0,
        survey.ans4:0
    }
    a=Answer.objects.filter(survey_idx=survey_idx)
    for answer in a:
        result[answer.ans]+=1
    return render(request, "survey/result.html", {'result': result})