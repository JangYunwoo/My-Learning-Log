from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        'numbers' : list(range(1,11))
    }

    return render(request, 'articles/index.html', context)

def detail(request, article_number):

    context = {
        'article_number': article_number
    }

    return render(request, 'articles/detail.html', context)