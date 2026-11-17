from django.urls import path
from . import views

urlpatterns = [
    path('', views.personagem_lista, name='personagem_lista'),
    path('criar/', views.personagem_criar, name='personagem_criar'),
    path('<int:id>/editar/', views.personagem_editar, name='personagem_editar'),
    path('<int:id>/deletar/', views.personagem_deletar, name='personagem_deletar'),
    path('<int:id>/', views.personagem_detalhe, name='personagem_detalhe'),
]