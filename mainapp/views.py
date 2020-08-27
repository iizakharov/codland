from django.utils import timezone
from django.shortcuts import render

from mainapp.models import Article


def main(request):
    title = 'главная'
    last_article = Article.objects.filter(created__lte=timezone.now()).order_by('created')[:1]
    articles = Article.objects.all().order_by('created')

    content = {
        'title': title,
        'last_article': last_article,
        'articles': articles,
    }

    return render(request, 'mainapp/index.html', content)
