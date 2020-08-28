from django.urls import path
from . import views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.main, name='index'),
    path('article/<int:pk>/', mainapp.article, name='article'),
    # path('article/add/', mainapp.AddArticle.as_view(), name='add_article'),
    path('article/add/', mainapp.add_article, name='add_article'),
]
