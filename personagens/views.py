from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import PersonagemForm

# Create your views here.
def personagem_lista(request):
    personagens = Personagem.objects.all()
    return render(request, 'personagens/personagem_lista.html', {'personagens': personagens})

def personagem_detalhe(request, id):
    personagem = get_object_or_404(Personagem, id=id)
    return render(request, 'personagens/personagem_detalhe.html', {'personagem': personagem})

def personagem_criar(request):
    if request.method == 'POST':
        form = PersonagemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personagem_lista')
    else:
        form = PersonagemForm()
    return render(request, 'personagens/personagem_form.html', {'form': form})

def personagem_editar(request, id):
    personagem = get_object_or_404(Personagem, id=id)
    if request.method == 'POST':
        form = PersonagemForm(request.POST, instance=personagem)
        if form.is_valid():
            form.save()
            return redirect('personagem_lista')
    else:
        form = PersonagemForm(instance=personagem)
    return render(request, 'personagens/personagem_form.html', {'form': form})

def personagem_deletar(request, id):
    personagem = get_object_or_404(Personagem, id=id)
    if request.method == 'POST':
        personagem.delete()
        return redirect('personagem_lista')
    return render(request, 'personagens/personagem_delete.html', {'personagem': personagem})