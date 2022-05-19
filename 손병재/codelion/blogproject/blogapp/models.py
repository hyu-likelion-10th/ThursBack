from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200) # 문자열, 최대길이 200
    body = models.TextField() # 대용량 문자열
    date = models.DateTimeField(auto_now_add=True) # 자동 추가

    def __str__(self):
        return self.title # Blog object가 아니라 글 제목이 보이게 하기.

    