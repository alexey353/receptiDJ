# Generated by Django 3.1.7 on 2021-04-05 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recepti', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Рецепт', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(upload_to='images/recepies', verbose_name='Изображения'),
        ),
    ]
