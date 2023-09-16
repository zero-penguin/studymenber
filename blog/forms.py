from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        # 最新のコメント　編集可能に
        fields = ('content','savepoint','stage')
        exclude = ('post',)
        labels= {
            'content':''
        }

        widgets = {
            'content': forms.Textarea(attrs={'class': 'rich-textarea'})
        }