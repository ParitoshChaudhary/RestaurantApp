from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from menu_app.models import Item as ItemList, Category, Cuisine


# Create your views here.
@login_required
def menu_list(request):
    item_list = ItemList.objects.all()
    category = Category.objects.all()
    cuisine = Cuisine.objects.all()
    context = {
        'items' : item_list,
        'category' : category,
        'cuisine' : cuisine
    }
    return render(request, 'menu_list.html', context)
