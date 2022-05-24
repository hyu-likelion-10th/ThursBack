from time import time
from django.shortcuts import render,redirect
from.models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm
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

def formcreate(request):
    if request.method == 'POST':
        form=BlogForm(request.POST)
        if form.is_valid():#유효한지 체크하게 해줌
            post = Blog()
            post.title = form.cleaned_data['title']#검증을 거친 깨끗한 데이터를 포스 타이틀 포스트객체의 타이틀에 저장
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
        form = BlogForm()
    else:
        form = BlogForm()
    return render(request, 'form_create.html', {'form':form}) #폼이라는 이름으로 저 흐트믈에 찍어주겠다 3번째 인자까지, 단 3번째는 딕셔너리 형태로
def modelformcreate(request):
    return

# Create your views here.
