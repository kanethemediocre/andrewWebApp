from django.shortcuts import render, redirect


def home_page(request):

    context = {}
    return render(request, 'UmoLaunchPad1.html', context)


def game_page(request):
    return redirect("https://kanethemediocre.github.io/")
