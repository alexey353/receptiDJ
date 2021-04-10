from django.shortcuts import render, redirect
from .models import Articles
from .forms import PredlForm
from django.views.generic import DetailView

def catalog(request):
    news = Articles.objects.all()
    return render(request, 'main\catalog.html', {'news': news})

class RecipesDetailView(DetailView):
    model = Articles
    template_name = 'recepti/detail_recept.html'
    context_object_name = 'article'


def create_recipes(request):
    error = ''
    if request.method == 'POST':
        form = PredlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
        else:
            error = 'Форма заполнена неверно'

    form = PredlForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'recepti\create_recipes.html', data)

def zakuski(request):
    zakus = Articles.objects.all()
    return render(request, 'recepti/zakuski.html', {'zakus': zakus})

def main_dish(request):
    zakus = Articles.objects.all()
    return render(request, 'recepti/main-dish.html', {'zakus': zakus})

def salads(request):
    zakus = Articles.objects.all()
    return render(request, 'recepti/salads.html', {'zakus': zakus})

def desserts(request):
    zakus = Articles.objects.all()
    return render(request, 'recepti/desserts.html', {'zakus': zakus})

def drinks(request):
    zakus = Articles.objects.all()
    return render(request, 'recepti/drinks.html', {'zakus': zakus})

def vegetarians(request):
    zakus = Articles.objects.all()
    return render(request, 'recepti/vegetarians.html', {'zakus': zakus})
