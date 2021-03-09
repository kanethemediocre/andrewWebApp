from django.shortcuts import render


def home_page(request):

    context = {}
    return render(request, 'UmoLaunchPad1.html', context)


def game_page(request):
   context = {}
   return render(request, 'UmoSpace151.html', context)