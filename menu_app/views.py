from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from menu_app.models import Item as ItemList, Category, Cuisine
from menu_app.forms import ItemForm, CategoryForm, CuisineForm
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
        itemform = ItemForm(request.POST or None)
        catform = CategoryForm(request.POST or None)
        cuisineform = CuisineForm(request.POST or None)
        if itemform.is_valid():
            item = itemform.save(commit=False)
            cat = catform.save(commit=False)
            item.name = request.POST.get('name')
            item.cost = request.POST.get('cost')
            cat.category_type = request.POST.get('category')
            item.save()
            cat.save()
            

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


def edit_item(request):
    pass


def delete_item(request):
    pass