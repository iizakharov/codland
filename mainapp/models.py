from django.db import models


class Article(models.Model):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['created']

    name = models.CharField(verbose_name='заголовок', max_length=64,
                            unique=True)
    description = models.TextField(verbose_name='полный текст статьи',
                                   blank=True)
    image = models.ImageField(upload_to='article_images',
                              verbose_name='иллюстрация', blank=True)
    # sort_description = models.TextField(verbose_name='краткий текст статьи',
    #                                     blank=True, max_length=90)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    is_active = models.BooleanField(verbose_name='статья активна',
                                    default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        short = self.description
        self.sort_description = short[:60]

        super().save(*args, **kwargs)
