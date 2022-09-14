from django.db import models
from django.conf import settings
from django.utils import timezone
class Post(models.Model):
    ip = models.CharField(max_length=128,default=None)
    tag = models.CharField(max_length=100)
    satisfaction = models.PositiveSmallIntegerField()
    postdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"날짜 : {self.postdate} 번호 : {self.id} 아이피 : {self.ip}"

class Board(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    user_name = models.EmailField()
    password = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    