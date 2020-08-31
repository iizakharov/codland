from django import forms
from django.contrib import admin

from mainapp.models import Article, NewArt

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewArtAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание",
                                  widget=CKEditorUploadingWidget())

    class Meta:
        model = NewArt
        fields = '__all__'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    list_display_links = ('name',)
    list_filter = ('name',)
    form = NewArtAdminForm


admin.site.register(NewArt)
