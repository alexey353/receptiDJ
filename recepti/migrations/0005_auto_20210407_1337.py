# Generated by Django 3.1.7 on 2021-04-07 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepti', '0004_articles_avtor'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='history',
            field=models.CharField(default='Италия', max_length=150, verbose_name='Страна происхождения:'),
        ),
        migrations.AddField(
            model_name='articles',
            name='kkal',
            field=models.CharField(default='150 ккал', max_length=50, verbose_name='Калорийность:'),
        ),
    ]
