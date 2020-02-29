from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def menu_list(request):
    context = {
        'add_item' : 'Please add your item here.'
    }
    return render(request, 'menu_list.html', context)
