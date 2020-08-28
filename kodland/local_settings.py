from pathlib import Path

SECRET_KEY = 'g%nx7ou=7cdo23lbyonu)_2v5b%uf6h!(m!-svq98cbagu@dc0'
DEBUG = True
ALLOWED_HOSTS = ['*']
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DOMAIN_NAME = 'http://127.0.0.1:8000'
