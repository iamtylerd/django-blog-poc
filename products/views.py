import imp
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm, RawProductForm
from .models import Product

# Create your views here.

# def product_create_view(request):
#     my_form = RawProductForm(request.POST)
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         if my_form.is_valid():
#             Product.objects.create(**my_form.cleaned_data)
#     context = {
#         "form": my_form
#     }
#     # Product.objects.create(title=title)
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
#     title = request.POST.get('title')
#     context = {}
#     # Product.objects.create(title=title)
#     return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     # context ={
#     #     'title': obj.title,
#     #     'description': obj.description
#     # }
#     context = {
#         'object': obj
#     }
#     return render(request, "products/product_detail.html", context)

def dynamic_lookup_view(request, id):
    obj = Product.objects.get(id=id)
    obj = get_object_or_404(Product, id=id)
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)