from .models import Predl
from django.forms import ModelForm, TextInput, DateInput, Textarea, ImageField

class PredlForm(ModelForm):
    class Meta:
        model = Predl
        fields = ['name_predl', 'category_predl', 'history_predl', 'full_text_predl', 'anons_predl', 'kkal_predl',
                  'avtor_predl']

        widgets = {
            "name_predl": TextInput(attrs={
                'class': 'form-predl',
                'placeholder': 'Название рецепта'
            }),
            "category_predl": TextInput(attrs={
                'class': 'form-predl',
                'placeholder': 'Категория'
            }),
            "history_predl": TextInput(attrs={
                'class': 'form-predl',
                'placeholder': 'Страна происхождения'
            }),
            "full_text_predl": Textarea(attrs={
                'class': 'form-predl-full',
                'placeholder': 'Рецепт'
            }),
            "anons_predl": TextInput(attrs={
                'class': 'form-predl-anons',
                'placeholder': 'Краткое описание блюда'
            }),
            "kkal_predl": TextInput(attrs={
                'class': 'form-predl',
                'placeholder': 'Калорийность'
            }),
            "avtor_predl": TextInput(attrs={
                'class': 'form-predl',
                'placeholder': 'Автор рецепта'
            })
        }