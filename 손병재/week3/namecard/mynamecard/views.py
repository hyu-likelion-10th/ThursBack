from django.shortcuts import render

# Create your views here.
def showNameCard(request):
    return render(request, 'index.html')