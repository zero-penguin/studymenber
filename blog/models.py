from django.conf import settings
from django.db import models
from django.utils import timezone

class ChoiceField(models.CharField):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        kwargs['max_length'] = 20  # max_length を追加
        super().__init__(*args, **kwargs, choices=choices)

# 記録のためのリレーションモデル
class Comment(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content
    
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=20)
    images = models.ImageField(upload_to="menber_face") # upload_toはどこのディレクトリに画像をアップロードするかの設定
    studyday_type = ChoiceField(choices=[
        ('火曜１７時', '火曜１７時'),
        ('火曜１８時', '火曜１８時'),
        ('水曜１７時', '水曜１７時'),
        ('水曜１８時', '水曜１８時'),
        ('金曜１７時', '金曜１７時'),
        ('金曜１８時', '金曜１８時'),
        ('土曜１０時', '土曜１０時'),
        ('土曜１１時', '土曜１１時'),
        ('土曜１３時', '土曜１３時'),
        ('土曜１４時', '土曜１４時'),
    ])
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE,blank=True,null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
