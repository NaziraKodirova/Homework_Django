from django.shortcuts import render

def theme_list(request):
    themes = open('lessons.txt').read().splitlines()
    return render(request, 'themes/theme_list.html', {'themes': themes})
