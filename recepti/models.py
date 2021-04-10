from django.db import models

class Articles(models.Model):
    name = models.CharField('Название блюда', max_length=150)
    category = models.CharField('Категория', max_length=100)
    history = models.CharField('Страна происхождения:', max_length=150, default="Италия")
    full_text = models.TextField('Рецепт')
    anons = models.CharField('Краткое описание блюда', max_length=250, default="Краткое описание блюда")
    kkal = models.CharField('Калорийность:', max_length=50, default="150 ккал")
    avtor = models.CharField('Автор рецепта', max_length=250, default="So Delicious")
    date = models.DateField('Дата публикации')
    image = models.ImageField('Изображения', upload_to='images/recepies')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

class Predl(models.Model):
    name_predl = models.CharField('Название блюда', max_length=150)
    category_predl = models.CharField('Категория', max_length=100)
    history_predl = models.CharField('Страна происхождения:', max_length=150, default="")
    full_text_predl = models.TextField('Рецепт')
    anons_predl = models.CharField('Краткое описание блюда', max_length=250, default="")
    kkal_predl = models.CharField('Калорийность:', max_length=50, default="")
    avtor_predl = models.CharField('Автор рецепта', max_length=250, default="")

    def __str__(self):
        return self.name_predl

    class Meta:
        verbose_name = 'Предложенный рецепт'
        verbose_name_plural = 'Предложенные рецепты'