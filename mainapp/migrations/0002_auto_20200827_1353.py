# Generated by Django 3.1 on 2020-08-27 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='sort_description',
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='article_images', verbose_name='иллюстрация'),
        ),
        migrations.AlterField(
            model_name='article',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='статья активна'),
        ),
    ]
