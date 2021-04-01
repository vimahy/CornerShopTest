from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.utils import timezone
from .models import Dish
from .forms import DishForm




@login_required
def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'dishes/dish_detail.html', {'dish': dish})
    
@login_required
def dish_new(request):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.save()
            return redirect('dish_detail', pk=dish.pk)
    else:
        form = DishForm()
    return render(request, 'dishes/dish_edit.html', {'form': form})

@login_required
def dish_edit(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    if request.method == "POST":
        form = DishForm(request.POST, instance=dish)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.save()
            return redirect('dish_detail', pk=dish.pk)
    else:
        form = DishForm(instance=dish)
    return render(request, 'dishes/dish_edit.html', {'form': form})
    

@login_required
def dish_delete(request, pk):
    context ={}
    dish = get_object_or_404(Dish,pk=pk)
    if request.method=="POST":
        dish.delete()
        return redirect('menu/')    
    return render(request, 'dishes/dish_delete.html',context )
