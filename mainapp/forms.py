from django import forms

from mainapp.models import Article


class ArticleForm(forms.ModelForm):
    """Форма статьи"""
    class Meta:
        model = Article
        # exclude = ('created', 'updated',)
        fields = ('name', 'sort_description', 'description', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
