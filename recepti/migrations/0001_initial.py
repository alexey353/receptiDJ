# Generated by Django 3.1.7 on 2021-04-05 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название блюда')),
                ('category', models.CharField(max_length=100, verbose_name='Категория')),
                ('full_text', models.TextField(verbose_name='Рецепт')),
                ('date', models.DateField(verbose_name='Дата публикации')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображения')),
            ],
        ),
    ]
