from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
    "title": "Random Business",
    }
    return render(request, 'home.html', context)