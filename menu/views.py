from django.shortcuts import render,redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from .models import Menu
from .forms import MenuForm

from .tasks import send




@login_required
def menu_list(request):
    menus = Menu.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'menu/menu_list.html', {'menus': menus})



@login_required
def menu_detail(request, unique_id):
    menu = get_object_or_404(Menu, unique_id=unique_id)
    return render(request, 'menu/menu_detail.html', {'menu': menu})


@login_required
def menu_send(request,pk):
    send(request,pk)
    return render(request, 'menu/menu_sent.html' )





           
@login_required
def menu_delete(request, pk):
    context ={}
    menu = get_object_or_404(Menu,pk=pk)
    if request.method=="POST":
        menu.delete()
        return redirect('menu/')    
    return render(request, 'menu/menu_delete.html',context )

@login_required
def menu_new(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('menu_detail', unique_id=menu.unique_id)
    else:
        form = MenuForm()
    return render(request, 'menu/menu_edit.html', {'form': form})


@login_required
def menu_edit(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('menu_detail', pk=menu.pk)
    else:
        form = MenuForm(instance=menu)
    return render(request, 'menu/menu_edit.html', {'form': form})
    



