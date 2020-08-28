SECRET_KEY = 'g%nx7ou=7cdo23lbyonu)_2v5b%uf6h!(m!-svq98cbagu@dc0'
DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'NAME': 'booking',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'book',
        'PASSWORD': 'book',
        'HOST': '89.108.65.47',
        'PORT': ''
    }
}
DOMAIN_NAME = '89-108-65-47.cloudvps.regruhosting.ru:8000'