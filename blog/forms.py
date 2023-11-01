from django import forms
from django.contrib.auth.models import User
from .models import Post,Comment,Account

class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Account
        fields = ('last_name','first_name',)
        labels = {'last_name':"苗字",'first_name':"名前",}

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # 最新のコメント　編集可能に
        fields = ('stage','content','savepoint',)
        exclude = ('post',)
        labels= {
            'content':''
        }

        widgets = {
            'author': forms.HiddenInput(),  # authorフィールドを非表示に
            'content': forms.Textarea(attrs={'class': 'rich-textarea', 'maxlength': '100'})
        }
        
class ChangeDayForm(forms.ModelForm):

    class Meta:
        model = Post
        # 最新のコメント　編集可能に
        fields = ('studyday_type',)
        labels= {
            'content':''
        }
        