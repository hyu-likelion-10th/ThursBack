import imp
from unittest import result
from xml.dom import INDEX_SIZE_ERR
from django.shortcuts import render
from survey.models import Survey, Answer
#from django.views.decorators.csrf import csrf_protect

# Create your views here.
def main(request):
    survey=Survey.objects.filter(status='y').order_by("-survey_idx")[0]
    return render(request, "main.html", {'survery':survey})

#@csrf_protect
def save_survey(request):
    dto=Answer(survey_idx=request.POST["survey_idx"], num=request.POST["num"])
    dto.save()
    return render(request, "success.html")


def show_result(request):
    idx = request.GET["survey_idx"]
    ans = Survey.objects.get(survey_idx = idx)
    answer = [ans.ans1, ans.ans2, ans.ans3, ans.ans4]
    surveyList = Survey.objects.raw("""
        select
            survey_idx, num, count(num) sum_num,
            round((select count(*) from survey_answer
            where survey_idx=a.survey_idx and num=a.num)*100.0/
            (select count(*) from survey_answer
                where survey_idx=a.survey_idx),1) rate
        from survey_answer a
        where survey_idx=%s
    group by survey_idx,num
    order by num
    """, idx)
    surveyList = zip(surveyList, answer)
    print("surveyList:", surveyList)
    print("answer:", answer)
    count= Answer.objects.all().count()
    return render(None, 'result.html', {"surveyList":surveyList, "count": count})
    