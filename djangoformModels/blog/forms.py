from django import forms

from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     article = forms.CharField(widget=forms.Textarea())
#     category = forms.CharField(max_length=50)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = ['title', 'article', 'category']
        fields = "__all__"