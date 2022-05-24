from django.shortcuts import render

def home(request):
    return render(request,'main.html')

def calculate(request):
    return render(request,'calculator.html')

def calculator(request):
    # GET으로 값을 받고, eval 함수를 사용해 값 계산
    formula = request.GET['formula']
    answer = eval(formula)
    # calculator 페이지 렌더링
    return render(request, 'calculator.html', {"answer":answer})
# Create your views here.
