from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView

from mainapp.forms import ArticleForm
from mainapp.models import Article


def get_article(pk):
    return get_object_or_404(Article, pk=pk)


def main(request):
    title = 'главная'
    last_article = Article.objects.filter(is_active=True).order_by('-created')[:1]
    articles = Article.objects.all().order_by('-created')[1:]

    content = {
        'title': title,
        'last_article': last_article,
        'articles': articles,
    }

    return render(request, 'mainapp/index.html', content)


def article(request, pk):
    context = {
        'title': 'продукт',
        'object': get_article(pk),
    }
    return render(request, 'mainapp/article.html', context)


def add_article(request):
    form = ArticleForm(request.POST, request.FILES)

    if request.method == "POST" and form.is_valid():
        name = request.POST['name']
        description = request.POST['description']
        image = request.FILES['image']

        Article.objects.create(name=name,
                               description=description,
                               sort_description=description[:190],
                               image=image,
                               is_active=False)

        return HttpResponseRedirect(reverse('main:index'))

    content = {
        'title': 'новая стать',
        'form': form,
    }
    return render(request, 'mainapp/add_article.html', content)
