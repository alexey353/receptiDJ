from django.db import models


class Instr(models.Model):
    name = models.CharField('Название инструмента', max_length=150)
    history = models.CharField('Страна происхождения:', max_length=150, default="")
    full_text = models.TextField('Описание')
    materials = models.TextField('Материалы', default="")
    date = models.DateField('Дата публикации')
    image = models.ImageField('Изображения', upload_to='images/instruments')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'