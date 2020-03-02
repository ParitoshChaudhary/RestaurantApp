from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from menu_app.models import Item as ItemList, Category, Cuisine
from menu_app.forms import ItemForm
from django.contrib import messages


# Create your views here.
@login_required
def menu_list(request):
    item_list = ItemList.objects.all()
    category = Category.objects.all()
    cuisine = Cuisine.objects.all()
    context = {
        'items': item_list,
        'category': category,
        'cuisine': cuisine
    }
    return render(request, 'menu_list.html', context)


@login_required()
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST or None)
        print(form.data['name'])
        print(form.data['cuisine'])
        print(form.data['category'])
        print(form.data['cost'])

        if form.is_valid():
            item = form.save(commit=False)
            item.name = form.data['name']
            item.cuisine = form.data['cuisine']
            item.category = form.data['category']
            item.cost = form.data['cost']
            item.save()
            messages.success(request, 'Item added successfully!!')
        else:
            messages.warning(request, 'Unable to add the item.')
        return redirect('add_item')

    else:
        item_list = ItemList.objects.all()
        category = Category.objects.all()
        cuisine = Cuisine.objects.all()
        context = {
            'items': item_list,
            'category': category,
            'cuisine': cuisine
        }
        return render(request, 'add_item.html', context)
