from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.instruments, name='instruments'),
    path('<int:pk>', views.InstrumentsDetailView.as_view(), name='instr-detail')
]