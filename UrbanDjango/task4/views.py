from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def platform_index(request):
    return render(request, 'platform.html')


class cart_index(TemplateView):
    template_name = 'cart.html'


def games_index(request):
    game_1 = "Atomic Heart"
    game_2 = "Cyberpunk 2077"
    game_3 = "PayDay"
    games = ["Atomic Heart", "Cyberpunk 2077", "PayDay"]
    context = {
        'game_1': game_1,
        'game_2': game_2,
        'game_3': game_3,
        'games' : games,
    }

    return render(request,'games.html', context)

class menu_index(TemplateView):
    template_name = 'menu.html'







# def cart_index(request):
#     return render(request, 'cart.html')
#
# def games_index(request):
#     return render(request, 'games.html')
#from django.shortcuts import render

# Create your views here.
