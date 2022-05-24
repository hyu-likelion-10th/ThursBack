from time import time
from django.shortcuts import render,redirect
from.models import Blog
from django.utils import timezone
def home(request):
    return render(request,'index.html')

def new(request):
    return render(request,'new.html')

def create(request):
    if(request.method == 'POST'):
        post=Blog()
        post.title=request.POST['title']
        post.body=request.POST['body']
        post.date=timezone.now()#시간 저장
        post.save()#다 했으면 저장해라
    return redirect('home')#이 함수 끝났으면 특정 함수로 리디렉트해라


# Create your views here.
