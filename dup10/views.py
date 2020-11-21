from django.shortcuts import render, get_object_or_404
from .models import Flower
from .forms import MyForm, TagsForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required

def index(request): # < here
    flowers = Flower.objects.all()
    q = request.GET.get('q', None)
    items = ''
    if q is None or q is "":
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)
    return render(request, 'dup10/index.html', {'flowers':flowers})
    
def detail(request, slug=None):
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'dup10/detail.html', {'flower':flower})
    
def tags(request, slug=None):
    flowers = Flower.objects.filter(tags__slug=slug)
    return render(request, 'dup10/index.html', {'flowers':flowers })
 
def create(request): # < here
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    return render(request, 'dup10/edit.html', {'form': form})
 
@permission_required('hay_app01.change_flower')
def edit(request, pk=None): # < here
    flower = get_object_or_404(Flower, pk=pk)
    if request.method == "POST":
        form = MyForm(request.POST, instance=flower)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm(instance=flower)
    return render(request, 'dup10/edit.html', {'form': form})

@permission_required('hay_app01.change_delete')
def delete(request, pk=None): # < here
    flower = get_object_or_404(Flower, pk=pk)
    flower.delete()
    return render(request, 'base/index.html')