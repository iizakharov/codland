from django.contrib.auth.models import User

from mainapp.models import Article

from django.core.management.base import BaseCommand

import json
import os

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r',
              encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        articles = load_from_json('articles')
        Article.objects.all().delete()
        [Article.objects.create(**article) for article in articles]

        # Создаем суперпользователя при помощи менеджера модели
        if not User.objects.filter(username='django').exists():
            User.objects.create_superuser('django', 'd@d.ru', '1')
