from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Produto
from home.forms import ProdutoForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    agora ={
        'agora' : datetime.now()
    }
    return render(request,'index.html', agora)

def produto(request):
    context = {
        'lista': Produto.objects.all(),
    }
    return render(request,'produto/lista.html',context)

def form_produto(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProdutoForm(request.POST)
            if form.is_valid():
                produto = form.save(commit=False)
                produto.nome = form.data['nome']
                produto.preco = form.data['preco']
                produto.save()
                return redirect('produto')
        else:
            form = ProdutoForm()
        context = {
            'form': form,
        }
        return render(request,'produto/formulario.html',context)
    else:
        return redirect('/admin')
def editar_produto(request, pk):
    if request.user.is_authenticated:
        produto = Produto.objects.get(pk=pk)
        if request.method == 'POST':
            form = ProdutoForm(request.POST, instance=produto)
            if form.is_valid():
                produto = form.save(commit=False)
                produto.nome = form.data['nome']
                produto.preco = form.data['preco']
                produto.save()
                return redirect('produto')
        else:
            form = ProdutoForm(instance=produto)
        context = {
            'form': form,
        }
        return render(request,'produto/formulario.html',context)
    else:
        return redirect('/admin')
def remover_produto(request, pk):
    if request.user.is_authenticated:
        produto = Produto.objects.get(pk=pk)
        if request.method == 'GET':
            produto.delete()
            return redirect('produto')
        return render(request,'produto/remover.html',{'produto':produto})
    else:
        return redirect('/admin')

@csrf_exempt
def detalhes_produto(request, pk):
    if request.user.is_authenticated:
        produto = Produto.objects.get(pk=pk)
        return render(request, 'produto/detalhes.html', {'produto': produto})
    else:
        return redirect('/admin')