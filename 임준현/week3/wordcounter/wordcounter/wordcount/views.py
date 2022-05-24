from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def getResult(request):
    inputText = request.GET['inputText']
    wordList = inputText.split()
    totalCnt = len(wordList)
    
    parsingResult = {}

    for word in wordList:
        if word in parsingResult:
            parsingResult[word] += 1
        else:
            parsingResult[word] = 1

    return render(request, "result.html", {"inputText":inputText, "totalCnt":totalCnt, "parsingResult":parsingResult})
