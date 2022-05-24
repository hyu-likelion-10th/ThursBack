from django.db import models

# Create your models here.
class Blog(models.Model):# 장고의 모델 기능 상속
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)#형식 지정

    def __str__(self):
        return self.title #타이틀이 보이게 설정
