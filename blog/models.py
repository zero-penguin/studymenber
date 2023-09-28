from django.conf import settings
from django.db import models
#ユーザー認証
from django.contrib.auth.models import User
from django.utils import timezone

class ChoiceField(models.CharField):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        kwargs['max_length'] = 100  # max_length を追加
        super().__init__(*args, **kwargs, choices=choices)

 
# ユーザーアカウントのモデルクラス
class Account(models.Model):

    # ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 追加フィールド
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
       
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    userid = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    katakana = models.CharField(max_length=200)
    school = models.CharField(max_length=20)
    images = models.ImageField(upload_to="member_face")
    studyday_type = models.CharField(
        max_length=100,
        choices=[
        ('Tuesday 17:00', 'Tuesday 17:00'),
        ('Tuesday 18:00', 'Tuesday 18:00'),
        ('Wednesday 17:00', 'Wednesday 17:00'),
        ('Wednesday 18:00', 'Wednesday 18:00'),
        ('Friday 17:00', 'Friday 17:00'),
        ('Friday 18:00', 'Friday 18:00'),
        ('Saturday 10:00', 'Saturday 10:00'),
        ('Saturday 11:00', 'Saturday 11:00'),
        ('Saturday 13:00', 'Saturday 13:00'),
        ('Saturday 14:00', 'Saturday 14:00'),
        ]
    )
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='Comment')
    content = models.CharField(max_length=200)
    savepoint = models.CharField(      
        max_length=10,
        choices=[
            ('not save', 'not save'),
            ('save', 'save'),
        ],
        default="not save",
    )
    stage = models.CharField(
        max_length=10,
        choices=[
            ('1-1-1', '1-1-1'),
            ('1-1-2', '1-1-2'),
            ('1-1-3', '1-1-3'),
            ('1-1-4', '1-1-4'),
            ('1-1-5', '1-1-5'),
            ('1-1-6', '1-1-6'),
            ('1-1-7', '1-1-7'),
            ('1-1-8', '1-1-8'),
            ('1-2-1', '1-2-1'),
            ('1-2-2', '1-2-2'),
            ('1-2-3', '1-2-3'),
            ('1-2-4', '1-2-4'),
            ('1-3-1', '1-3-1'),
            ('1-3-2', '1-3-2'),
            ('1-3-3', '1-3-3'),
            ('1-3-4', '1-3-4'),
            ('1-4-1', '1-4-1'),
            ('1-4-2', '1-4-2'),
            ('1-4-3', '1-4-3'),
            ('1-4-4', '1-4-4'),
            ('2-1-1', '2-1-1'),
            ('2-1-2', '2-1-2'),
            ('2-1-3', '2-1-3'),
            ('2-1-4', '2-1-4'),
            ('2-2-1', '2-2-1'),
            ('2-2-2', '2-2-2'),
            ('2-2-3', '2-2-3'),
            ('2-2-4', '2-2-4'),
            ('2-3-1', '2-3-1'),
            ('2-3-2', '2-3-2'),
            ('2-3-3', '2-3-3'),
            ('2-3-4', '2-3-4'),
            ('2-4-1', '2-4-1'),
            ('2-4-2', '2-4-2'),
            ('2-4-3', '2-4-3'),
            ('2-4-4', '2-4-4'),
            ('3-1-1', '3-1-1'),
            ('3-1-2', '3-1-2'),
            ('3-1-3', '3-1-3'),
            ('3-1-4', '3-1-4'),
            ('3-2-1', '3-2-1'),
            ('3-2-2', '3-2-2'),
            ('3-2-3', '3-2-3'),
            ('3-2-4', '3-2-4'),
            ('3-3-1', '3-3-1'),
            ('3-3-2', '3-3-2'),
            ('3-3-3', '3-3-3'),
            ('3-3-4', '3-3-4'),
            ('3-4-1', '3-4-1'),
            ('3-4-2', '3-4-2'),
            ('3-4-3', '3-4-3'),
            ('3-4-4', '3-4-4'),
            ('初級検定','初級検定'),
            ('4-1-1', '4-1-1'),
            ('4-1-2', '4-1-2'),
            ('4-1-3', '4-1-3'),
            ('4-1-4', '4-1-4'),
            ('4-2-1', '4-2-1'),
            ('4-2-2', '4-2-2'),
            ('4-2-3', '4-2-3'),
            ('4-2-4', '4-2-4'),
            ('4-3-1', '4-3-1'),
            ('4-3-2', '4-3-2'),
            ('4-3-3', '4-3-3'),
            ('4-3-4', '4-3-4'),
            ('4-4-1', '4-4-1'),
            ('4-4-2', '4-4-2'),
            ('4-4-3', '4-4-3'),
            ('4-4-4', '4-4-4'),
            ('5-1-1', '5-1-1'),
            ('5-1-2', '5-1-2'),
            ('5-1-3', '5-1-3'),
            ('5-1-4', '5-1-4'),
            ('5-2-1', '5-2-1'),
            ('5-2-2', '5-2-2'),
            ('5-2-3', '5-2-3'),
            ('5-2-4', '5-2-4'),
            ('5-3-1', '5-3-1'),
            ('5-3-2', '5-3-2'),
            ('5-3-3', '5-3-3'),
            ('5-3-4', '5-3-4'),
            ('5-4-1', '5-4-1'),
            ('5-4-2', '5-4-2'),
            ('5-4-3', '5-4-3'),
            ('5-4-4', '5-4-4'),
            ('6-1-1', '6-1-1'),
            ('6-1-2', '6-1-2'),
            ('6-1-3', '6-1-3'),
            ('6-1-4', '6-1-4'),
            ('6-2-1', '6-2-1'),
            ('6-2-2', '6-2-2'),
            ('6-2-3', '6-2-3'),
            ('6-2-4', '6-2-4'),
            ('6-3-1', '6-3-1'),
            ('6-3-2', '6-3-2'),
            ('6-3-3', '6-3-3'),
            ('6-3-4', '6-3-4'),
            ('6-4-1', '6-4-1'),
            ('6-4-2', '6-4-2'),
            ('6-4-3', '6-4-3'),
            ('6-4-4', '6-4-4'),
            ('中級検定','中級検定'),
            ('7-1-1', '7-1-1'),
            ('7-1-2', '7-1-2'),
            ('7-1-3', '7-1-3'),
            ('7-1-4', '7-1-4'),
            ('7-2-1', '7-2-1'),
            ('7-2-2', '7-2-2'),
            ('7-2-3', '7-2-3'),
            ('7-2-4', '7-2-4'),
            ('7-3-1', '7-3-1'),
            ('7-3-2', '7-3-2'),
            ('7-3-3', '7-3-3'),
            ('7-3-4', '7-3-4'),
            ('7-4-1', '7-4-1'),
            ('7-4-2', '7-4-2'),
            ('7-4-3', '7-4-3'),
            ('7-4-4', '7-4-4'),
        ]
    )

    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.content

class Slide(models.Model):
    contact = models.TextField()
    image = models.ImageField(upload_to="contact_image")  # 画像データを保存するフィールド
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.content
