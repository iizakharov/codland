from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Article(models.Model):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['created']

    name = models.CharField(verbose_name='заголовок', max_length=64)
    description = models.TextField(verbose_name='полный текст статьи',
                                   blank=True)
    description1 = RichTextUploadingField(verbose_name='полный текст статьи',
                                          blank=True, null=True)
    image = models.ImageField(upload_to='article_images',
                              verbose_name='иллюстрация', blank=True)
    sort_description = models.TextField(verbose_name='краткий текст статьи',
                                        blank=True, max_length=190)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    # slug = models.SlugField(default='', blank=True)
    is_active = models.BooleanField(verbose_name='статья активна',
                                    default=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class NewArt(models.Model):
    name = models.CharField(verbose_name='заголовок', max_length=64,
                            unique=True)
    content = RichTextField()
    content2 = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return self.name
