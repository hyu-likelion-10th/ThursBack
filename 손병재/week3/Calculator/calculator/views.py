from django.shortcuts import render


# Create your views here.

def main(request):
    # 메인페이지 렌더링
    return render(request, 'calculator/main.html')

def calculator(request):
    # GET으로 값을 받고, eval 함수를 사용해 값 계산
    formula = request.GET['formula']
    answer = eval(formula)
    # calculator 페이지 렌더링
    return render(request, 'calculator/calculator.html', {"answer":answer})
