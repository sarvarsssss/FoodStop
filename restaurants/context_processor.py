from django.shortcuts import get_object_or_404
from restaurants.models import CarSell

def categories(request):
    cat_list = []
    all_cat = CarSell.objects.all()
    for cat in all_cat:
        name_list = cat.categories.split(',')
        for item in name_list:
            cat_list.append(item)
    cat_dict = {'categories': set(cat_list)}
    return cat_dict

def user_liked_posts(request):
    if request.user.is_authenticated:
        posts = CarSell.objects.filter(likes=request.user.id)
        return {'user_liked_posts': posts}
    else:
        return {'user_liked_posts': None}

def recent_posts(request):
    posts = CarSell.objects.all().order_by('-created_at')[:5]
    return {'recent_posts': posts}

