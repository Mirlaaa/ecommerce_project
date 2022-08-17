from django.shortcuts import render,get_object_or_404, get_list_or_404
from .models import * 

# Create your views here.
def index(request):

  produtos = Produto.objects.all()[:4]
  context ={
    'destaques': produtos
  }
  for produto in context['destaques']:
    print(produto) 

  return render (request, 'index.html', context)

def listar_produtos(request):

  produtos = Produto.objects.all()

  context ={
    'produtos': produtos
  }
  print(context['produtos'].count())

  return render (request, 'produtos.html', context)

def produto_info(request, pk):
  print(f'PK: {pk}')
  
  produto = get_object_or_404(Produto, id = pk)
  
  context = {
    'produto': produto
  }

  return render (request, 'produto_info.html', context)

def listar_categoria(request, categoria: str):
  categoria = categoria.title()
  print(f'Categoria: {categoria}')
  
  try:
    categoria_obj = Categoria.objects.get(nome=categoria)

    produtos = Produto.objects.filter(categoria=categoria_obj.id)

    context = {
      'produtos': produtos
    }

    for produto in context['produtos']:
      print(produto)     

    return render (request, 'categoria_produtos.html', context)
  except Categoria.DoesNotExist:
    return render(request, "error.html")

def sobre(request):
  return render(request, 'sobre.html')