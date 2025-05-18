from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto
from .forms import CategoriaForm, ProductoForm

# ---------- CATEGORÍA ----------

def categoria_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'tienda/categoria_list.html', {'categorias': categorias})

def categoria_form(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm()
    return render(request, 'tienda/categoria_form.html', {'form': form})

def categoria_editar(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'tienda/categoria_form.html', {'form': form})

def categoria_eliminar(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')
    return render(request, 'tienda/confirmar_eliminar.html', {
        'obj': categoria,
        'tipo': 'Categoría',
        'return_url': 'categoria_list'  # ✅ añadido para redirigir bien desde el template
    })

# ---------- PRODUCTO ----------

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/producto_list.html', {'productos': productos})

def producto_form(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'tienda/producto_form.html', {'form': form})

def producto_editar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'tienda/producto_form.html', {'form': form})

def producto_eliminar(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'tienda/confirmar_eliminar.html', {
        'obj': producto,
        'tipo': 'Producto',
        'return_url': 'producto_list'  # ✅ añadido para redirigir bien desde el template
    })
