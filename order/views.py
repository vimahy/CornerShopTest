import time

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect

from django.conf import settings

from .models import Order
from .forms import OrderForm


@login_required
def order_list(request):
    orders = Order.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'order/order_list.html', {'orders': orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order/order_detail.html', {'order': order})

def order_unavailable(request):
    return render(request, 'order/order_unavailable.html')




def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if time.strftime('%H:%M') < settings.LIMIT_TIME:
           return redirect('order_unavailable',)
        elif form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
    return render(request, 'order/order_edit.html', {'form': form})


def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'order/order_edit.html', {'form': form})
    

def order_delete(request, pk):
    context ={}
    order = get_object_or_404(Order,pk=pk)
    if request.method=="POST":
        order.delete()
        return redirect('order/')    
    return render(request, 'order/order_delete.html',context )
