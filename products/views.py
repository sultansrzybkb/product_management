from django.http import HttpResponse
from .forms import ProductForm
from .models import Product
from django.shortcuts import get_object_or_404, redirect, render
def product_list(request):
    product = Product.objects.all()
    return render(request,'products/product_list.html', {'products': product})
def product_detail(request,pk):
    product= get_object_or_404(Product,pk=pk)
    return render(request,'products/product_detail.html',{'product':product})
def product_create(request):
    if request.method== 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form= ProductForm()
    return render(request,'products/product_form.html', {'form': form})           
def product_update(request,pk):
    product =get_object_or_404(Product,pk=pk)
    if request.method=='POST':
        form =ProductForm(request.POST,instance=product)
        if  form_is_valid():  # type: ignore
            form.save()
            return redirect('product_list')
        else:
            form= ProductForm(instance=product)
            return render (request,'products/product_form.html')
def product_delete(request,pk):
    product =get_object_or_404(Product,pk=pk)
    if request.method== 'POST':
        product.delete()
        return redirect('product_list')
    return render(request,'product/product_confirm_delete.html',{'products':product})
def home(request):
    return HttpResponse('bu sayfa')