from django.shortcuts import render, redirect
from .models import Instr
from django.views.generic import DetailView

def instruments(request):
    inst = Instr.objects.all()
    return render(request, 'main\instruments.html', {'inst': inst})

class InstrumentsDetailView(DetailView):
    model = Instr
    template_name = 'instruments/detail_instr.html'
    context_object_name = 'instr'