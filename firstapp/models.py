from django.db import models

# 테이블명 -> firstapp_curriculum
class Curriculum(models.Model):
    # 기본키가 없으면 id 컬럼 자동 생성
    name = models.CharField(max_length=255)
    # score = models.CharField(max_length=255, null = True)



