from django.db import models
# 테이블명 --> secondapp_course
class Course(models.Model):
    # 기본키가 없으면 id 컬럼 자동 생성
    name = models.CharField(max_length=30) 
    cnt = models.IntegerField()