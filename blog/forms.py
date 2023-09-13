from django import forms

from .models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Comment
        # 最新のコメント　編集可能に
        fields = ('content',)