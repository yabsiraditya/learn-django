from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = ['title', 'article', 'category']
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update(
            {
                'class':'form-control'
            }
        )
        self.fields['article'].widget.attrs.update(
            {
                'class':'form-control'
            }
        )
        self.fields['category'].widget.attrs.update(
            {
                'class':'form-select'
            }
        )
        self.fields['writer'].widget.attrs.update(
            {
                'class':'form-control'
            }
        )